from __future__ import annotations

from typing import Literal, Dict, List

from pydantic import BaseModel, Field

from jsonschema_converter.types.types import JSONType


class JsonSchemaModel(BaseModel):

    type: JSONType | None = None
    items: JsonSchemaModel | None = None
    required: List[str] | None = None
    properties: Dict[str, JsonSchemaModel] | None = None
    format: Literal["email", "date", "date-time"] | None = None
    description: str | None = None
    id: str | None = Field(alias="$id", default=None)
    any_of: List[JsonSchemaModel] | None = Field(alias="anyOf", default=None)
    enum: List[str | int ] | None = None
