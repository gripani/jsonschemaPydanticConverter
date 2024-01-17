from os.path import join
from typing import Tuple, List

from jsonschema_converter.models.pydantic_schema_model import PydanticSchemaModel


class ClassWriter:

    def __init__(self, schema: PydanticSchemaModel):
        self._schema = schema

        attr_names = self.schema.properties.keys()

        self.required_dict = {name: False for name in attr_names}
        if self.schema.required is not None:
            for name in self.schema.required:
                self.required_dict[name] = True

    @property
    def schema(self) -> PydanticSchemaModel:
        return self._schema

    def write(self, file_name: str):

        pre_import_str = ""
        import_str = ""
        import_classes: List[Tuple[str, str]] = []
        post_import_str = ""

        attr_types = []
        for attribute in self.schema.properties.values():
            attr_types.append(attribute.type)
        attr_types = set(attr_types)

        typing_imports = {
            check_import: check_import in attr_types
            for check_import in ["Union", "List", "Literal"]
        }

        if any(typing_imports.values()):
            pre_import_str += "from typing import " + ", ".join(
                [key for key, val in typing_imports.items() if val]
            )
            pre_import_str += '\n'
            pre_import_str += '\n'
        pre_import_str += "from pydantic import BaseModel"
        pre_import_str += '\n'
        pre_import_str += '\n'

        post_import_str += '\n'
        post_import_str += f"class {self.schema.class_name}(BaseModel):"
        post_import_str += '\n'

        if self.schema.description is not None:
            post_import_str += "\t\"\"\"\n" + '\t' + self.schema.description + '\n\t' + "\"\"\""

        post_import_str += '\n'

        for attribute_name, attribute in self.schema.properties.items():
            sub_str, import_class = self._format_attribute(attribute_name, attribute)
            post_import_str += sub_str
            post_import_str += '\n'
            if import_class is not None:
                import_classes.append(import_class)

        if len(import_classes) > 0:
            for import_class in import_classes:
                import_str += "from schemas."
                import_str += import_class[0] + " import " + import_class[1]
                import_str += '\n'
            import_str += '\n'

        string = pre_import_str + import_str + post_import_str

        with open(join("schemas", file_name), "w") as f:
            f.write(string)

    def _format_attribute(self, attribute_name: str, attribute: PydanticSchemaModel) -> Tuple[str, Tuple[str, str] | None]:

        string = ""
        import_class: Tuple[str, str] | None = None

        if attribute.type != "object":
            attribute_type = attribute.type
        else:
            if attribute.class_name is not None:
                attribute_type = attribute.class_name
                import_class = attribute.name, attribute.class_name
            else:
                raise ValueError("class name cannot be none for attribute object")
        string += '\t' + attribute_name + ": " + attribute_type

        if attribute.type == "Literal":
            string += "["
            if attribute.enum is not None:
                sub_str = ""
                for sub_type in attribute.enum:
                    if isinstance(sub_type, str):
                        sub_str += "\"" + sub_type + "\"" + ", "
                    else:
                        sub_str += str(sub_type) + ", "
            else:
                raise AttributeError(f"{attribute} is not a valid Literal")
            string += sub_str[:-2] + "]"

        if attribute.type == "Union":
            string += "["
            if attribute.any_of is not None:
                sub_str = ""
                for any_of in attribute.any_of:
                    sub_str += "\"" + any_of.type + "\"" + ", "
                string += sub_str[:-2] + "]"
            else:
                raise AttributeError(f"{attribute} is not a valid Union")

        if attribute.type == "List":
            sub_attribute = attribute.items
            if sub_attribute.type != "object":
                sub_attribute_type = sub_attribute.type
            else:
                if sub_attribute.class_name is not None:
                    sub_attribute_type = sub_attribute.class_name
                    import_class = sub_attribute.name, sub_attribute.class_name
                else:
                    raise ValueError("class name cannot be None for attribute of type object")

            if sub_attribute.type == "Union":
                sub_attribute_type += "["
                sub_sub_str = ""
                for any_of in sub_attribute.any_of:
                    sub_sub_str += any_of.type + ", "
                sub_attribute_type += sub_sub_str[:-2] + "]"

            if sub_attribute.type == "Literal":
                sub_attribute_type += "["
                sub_sub_str = ""
                for enum in sub_attribute.enum:
                    if isinstance(enum, str):
                        sub_sub_str += "\"" + enum + "\"" + ", "
                    else:
                        sub_sub_str += str(enum) + ", "
                sub_attribute_type += sub_sub_str[:-2] + "]"

            string += "[" + sub_attribute_type + "]"

        if not self.required_dict[attribute_name]:
            string += " | None = None"

        return string, import_class
