from pydantic import BaseModel


class PdbxReferenceEntitySrcNatItem(BaseModel):

	atcc: str | None = None
	db_code: str | None = None
	db_name: str | None = None
	ordinal: int
	organism_scientific: str | None = None
	prd_id: str
	ref_entity_id: str
	source: str | None = None
	source_id: str | None = None
	taxid: str | None = None
