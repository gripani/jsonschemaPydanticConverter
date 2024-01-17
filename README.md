# JSONSchema Converter

JSONSchema Converter is a tool that performs 
conversions from a json-schema file to pydantic classes

## installation
```bash
pip install jsonschema-converter
```

## usage

*main.py*
```python
from argparse import ArgumentParser

from jsonschema_converter.parse import parse_json


def main(file_name: str):
    parse_json(file_name)


def parse_args():
    argument_parser = ArgumentParser(
        prog="JsonSchema2Pydantic",
        description="creates classes from json_schema file"
    )
    argument_parser.add_argument("file_name")
    args = argument_parser.parse_args()
    return args.file_name


if __name__ == "__main__":
    main(parse_args())
```

```bash
python main.py myjsonschema.json
```

## examples
you can find examples of jsonschema input and pydantic classes output in the examples folder
