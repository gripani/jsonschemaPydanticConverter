from pydantic import BaseModel


class RcsbSchemaContainerIdentifiersItem(BaseModel):

	collection_name: str
	collection_schema_version: str | None = None
	schema_name: str
