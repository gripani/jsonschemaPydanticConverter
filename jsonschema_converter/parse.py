from json import load
from os import mkdir
from os.path import exists, join

from jsonschema_converter.schema_parser import SchemaParser


def parse_json(file_name: str):

    with open(file_name, "r") as f:
        schema = load(f)

    if not exists("schemas"):
        mkdir("schemas")

    with open(join("schemas", "__init__.py"), "w") as f0:
        f0.write("")

    try:
        schema_parser = SchemaParser(schema, name=file_name.split(".json")[0])
    except ValueError as err:
        print(err)
        exit()
    schema_parser.parse()
