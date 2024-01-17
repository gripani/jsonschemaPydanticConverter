from typing import Literal

from pydantic import BaseModel


class RcsbChemCompRelatedItem(BaseModel):

	comp_id: str
	ordinal: int
	related_mapping_method: Literal["assigned by DrugBank resource", "assigned by PDB", "assigned by PubChem resource", "matching ChEMBL ID in Pharos", "matching InChIKey in DrugBank", "matching InChIKey in PubChem", "matching InChIKey-prefix in DrugBank", "matching by RESID resource"] | None = None
	resource_accession_code: str | None = None
	resource_name: Literal["CAS", "CCDC/CSD", "COD", "ChEBI", "ChEMBL", "DrugBank", "Pharos", "PubChem", "RESID"] | None = None
