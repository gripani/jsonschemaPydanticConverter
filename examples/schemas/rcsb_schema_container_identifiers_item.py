from pydantic import BaseModel


class RcsbSchemaContainerIdentifiersItem(BaseModel):
	"""
	RcsbSchemaContainerIdentifiersItem class

	Attributes
	----------
	collection_name:  `str`
		Collection name associated with the data in the container.
	collection_schema_version:  `str`
		Version string for the schema and collection.
	schema_name:  `str`
		Schema name associated with the data in the container.

	"""
	collection_name: str
	collection_schema_version: str | None = None
	schema_name: str
