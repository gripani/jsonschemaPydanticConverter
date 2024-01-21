from jsonschema_converter.main_parser import parse_json_schema
from jsonschema_converter.utils import parse_args


def convert():
    file_name, module_name, verbose = parse_args()
    parse_json_schema(file_name, module_name, verbose)
