from typing import Literal

from pydantic import BaseModel


class RcsbChemCompSynonymsItem(BaseModel):

	comp_id: str
	name: str | None = None
	ordinal: int
	provenance_source: Literal["ACDLabs", "Author", "ChEBI", "ChEMBL", "DrugBank", "GMML", "Lexichem", "OpenEye OEToolkits", "OpenEye/Lexichem", "PDB Reference Data", "PDB Reference Data (Preferred)", "PDB-CARE", "PubChem", "RESID"] | None = None
	type: Literal["Brand Name", "Common Name", "Condensed IUPAC Carbohydrate Symbol", "IUPAC Carbohydrate Symbol", "Preferred Common Name", "Preferred Name", "Preferred Synonym", "SNFG Carbohydrate Symbol", "Synonym", "Systematic Name"] | None = None
