from pydantic import BaseModel


class PdbxReferenceMoleculeListItem(BaseModel):

	family_prd_id: str
	prd_id: str
