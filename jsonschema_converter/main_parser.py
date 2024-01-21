from json import load
from os import mkdir
from os.path import exists, join
from sys import stderr

from loguru import logger

from jsonschema_converter.const import FORMAT
from jsonschema_converter.schema_parser import SchemaParser

logger.remove()
logger.add(stderr, level="INFO", format=FORMAT)


def parse_json_schema(file_name: str,
                      module_name: str | None = None,
                      verbose: bool | None = None):

    if module_name is None:
        module_name = "schemas"

    if verbose is None:
        verbose = False

    with open(file_name, "r") as f:
        schema = load(f)

    if not exists(module_name):
        mkdir(module_name)
        with open(join(module_name, "__init__.py"), "w") as f0:
            f0.write("")

    try:
        schema_parser = SchemaParser(schema, name=file_name.split(".json")[0])
        schema_parser.parse(module_name, verbose)
    except ValueError as err:
        detail=str(err)
        logger.error(f"parse_json - ValueError:\n{detail=}")
        exit()
