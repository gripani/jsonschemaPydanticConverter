from typing import Literal

from pydantic import BaseModel


class RcsbChemCompSynonymsItem(BaseModel):
	"""
	RcsbChemCompSynonymsItem class

	Attributes
	----------
	comp_id:  `str`
		The chemical component to which this synonym applies.
	name:  `str`
		The synonym of this particular chemical component.
	ordinal:  `int`
		This data item is an ordinal index for the
		 RCSB_CHEM_COMP_SYNONYMS category.
	provenance_source:  `Literal`
		The provenance of this synonym.
	type:  `Literal`
		This data item contains the synonym type.

	"""
	comp_id: str
	name: str | None = None
	ordinal: int
	provenance_source: Literal["ACDLabs", "Author", "ChEBI", "ChEMBL", "DrugBank", "GMML", "Lexichem", "OpenEye OEToolkits", "OpenEye/Lexichem", "PDB Reference Data", "PDB Reference Data (Preferred)", "PDB-CARE", "PubChem", "RESID"] | None = None
	type: Literal["Brand Name", "Common Name", "Condensed IUPAC Carbohydrate Symbol", "IUPAC Carbohydrate Symbol", "Preferred Common Name", "Preferred Name", "Preferred Synonym", "SNFG Carbohydrate Symbol", "Synonym", "Systematic Name"] | None = None
