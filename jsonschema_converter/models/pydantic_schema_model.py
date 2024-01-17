from __future__ import annotations

from typing import Literal, Dict, List

from pydantic import BaseModel

from jsonschema_converter.types.types import PythonType


class PydanticSchemaModel(BaseModel):

    type: PythonType
    name: str

    class_name: str | None = None
    items: PydanticSchemaModel | None = None
    required: List[str] | None = None
    properties: Dict[str, PydanticSchemaModel] | None = None
    format: Literal["email", "date", "date-time"] | None = None
    enum: List[str | int] | None = None
    any_of: List[PydanticSchemaModel] | None = None
    description: str | None = None
