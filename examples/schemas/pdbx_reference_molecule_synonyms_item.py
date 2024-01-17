from pydantic import BaseModel


class PdbxReferenceMoleculeSynonymsItem(BaseModel):

	family_prd_id: str
	name: str | None = None
	ordinal: int
	prd_id: str
	source: str | None = None
