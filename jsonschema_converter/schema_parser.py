from re import Match, sub

from pydantic import ValidationError
from loguru import logger

from jsonschema_converter.class_writer import ClassWriter
from jsonschema_converter.models.json_schema_model import JsonSchemaModel
from jsonschema_converter.models.pydantic_schema_model import PydanticSchemaModel
from jsonschema_converter.types.types import JSONType, PythonType


class SchemaParser:

    @staticmethod
    def from_json_to_pydantic_types(val: JSONType | None = None) -> PythonType:
        if val is None:
            return "Union"
        if val == "object":
            return "object"
        if val == "number":
            return "float"
        if val == "integer":
            return "int"
        if val == "string":
            return "str"
        if val == "array":
            return "List"

    @staticmethod
    def underscore_to_camelcase(field_name: str) -> str:
        def repl(match: Match[str]) -> str:
            letter = match.group(1)
            capital_letter = letter.upper()
            return capital_letter
        pattern = r"(?!^)_([a-zA-Z])"
        camelcase = sub(pattern, repl, field_name)

        return camelcase[0].upper() + camelcase[1:]

    def __init__(self, schema: dict | JsonSchemaModel, name: str):
        self._schema = schema
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def schema(self) -> JsonSchemaModel:
        if isinstance(self._schema, dict):
            try:
                return JsonSchemaModel.model_validate(self._schema)
            except ValidationError as err:
                raise ValueError(f"schema is not a valid json schema:\n{str(err)}") from err
        return self._schema

    def parse(self, module_name: str, verbose: bool) -> PydanticSchemaModel:
        if verbose:
            logger.info(f"parse - {self.name}")
        original_json = self.schema
        if original_json.type is not None:
            pydantic_type = SchemaParser.from_json_to_pydantic_types(original_json.type)
            any_of = None
        else:
            if original_json.any_of is not None:
                pydantic_type = SchemaParser.from_json_to_pydantic_types()
                any_of = [
                    SchemaParser(any_of, "union").parse(module_name, verbose)
                    for any_of in original_json.any_of
                ]
            else:
                raise ValueError("schema has no 'type' nor 'anyOf' field")
        original_pydantic = PydanticSchemaModel(
            name=self.name,
            type=pydantic_type,
            required=original_json.required,
            format=original_json.format,
            enum=original_json.enum,
            any_of=any_of,
            description=original_json.description
        )

        if original_pydantic.type == "object":
            original_pydantic.class_name = SchemaParser.underscore_to_camelcase(self.name)

        if original_json.properties is not None:
            original_pydantic.properties = dict()
            for property_name, property_schema in original_json.properties.items():
                check_pr1 = property_name == "class"
                check_pr2 = property_name.startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
                check_pr3 = property_name.startswith("model_")
                if check_pr1 or check_pr2 or check_pr3:
                    property_name = "_" + property_name

                property_parser = SchemaParser(property_schema, property_name)
                original_pydantic.properties[property_name] = property_parser.parse(module_name, verbose)

        if original_pydantic.type == "List":
            if original_json.items.type == "object":
                name = self.name + "_item"
                items_parser = SchemaParser(original_json.items, name)
                original_pydantic.items = items_parser.parse(module_name, verbose)
            else:
                items_parser = SchemaParser(original_json.items, "list")
                original_pydantic.items = items_parser.parse(module_name, verbose)

        if original_pydantic.enum is not None:
            original_pydantic.type = "Literal"

        if original_pydantic.type == "object":
            ClassWriter(original_pydantic).write(self.name + ".py", module_name)
        return original_pydantic
