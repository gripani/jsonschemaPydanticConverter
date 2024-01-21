# JSONSchema Converter

JSONSchema Converter is a tool that performs 
conversions from a json-schema file to pydantic classes

## installation
```bash
pip install jsonschema-converter
```

## usage

script *main.py*
```python
from jsonschema_converter.parse import parse_json_schema
from jsonschema_converter.utils import parse_args


if __name__ == "__main__":
    file_name, module_name = parse_args()
    parse_json_schema(file_name, module_name)


```

CLI
```bash
python main.py --file_name myjsonschema.json --module_name schemas
```

## examples
you can find examples of jsonschema input and pydantic classes output in the examples folder
