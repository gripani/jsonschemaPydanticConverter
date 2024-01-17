from pydantic import BaseModel


class PdbxReferenceMoleculeFeaturesItem(BaseModel):

	family_prd_id: str
	ordinal: int
	prd_id: str
	source: str | None = None
	source_ordinal: int | None = None
	type: str | None = None
	value: str | None = None
