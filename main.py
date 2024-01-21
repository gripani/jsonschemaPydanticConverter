from jsonschema_converter.parse import parse_json_schema
from jsonschema_converter.utils import parse_args


if __name__ == "__main__":
    file_name, module_name = parse_args()
    parse_json_schema(file_name, module_name)
