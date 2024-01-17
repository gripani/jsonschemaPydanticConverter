from pydantic import BaseModel


class PdbxReferenceMoleculeAnnotationItem(BaseModel):

	family_prd_id: str
	ordinal: int
	prd_id: str | None = None
	source: str | None = None
	text: str | None = None
	type: str | None = None
