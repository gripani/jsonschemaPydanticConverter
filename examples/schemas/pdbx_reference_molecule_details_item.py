from pydantic import BaseModel


class PdbxReferenceMoleculeDetailsItem(BaseModel):

	family_prd_id: str
	ordinal: int
	source: str | None = None
	source_id: str | None = None
	text: str | None = None
