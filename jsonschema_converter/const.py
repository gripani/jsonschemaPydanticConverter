from typing import Final

FORMAT : Final[str] = "{time:YYYY-MM-DD HH:mm:ss} | {level} | jsonschema-converter | {message}"
PROG_NAME: Final[str] = "JsonSchema2Pydantic"
PROG_DESCRIPTION: Final[str] = "creates classes from json_schema file"