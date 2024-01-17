from pydantic import BaseModel


class PdbxReferenceMoleculeRelatedStructuresItem(BaseModel):

	citation_id: str | None = None
	db_accession: str | None = None
	db_code: str | None = None
	db_name: str | None = None
	family_prd_id: str
	formula: str | None = None
	name: str | None = None
	ordinal: int
