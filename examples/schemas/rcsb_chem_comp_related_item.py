from typing import Literal

from pydantic import BaseModel


class RcsbChemCompRelatedItem(BaseModel):
	"""
	RcsbChemCompRelatedItem class

	Attributes
	----------
	comp_id:  `str`
		The value of _rcsb_chem_comp_related.comp_id is a reference to
		 a chemical component definition.
	ordinal:  `int`
		The value of _rcsb_chem_comp_related.ordinal distinguishes
		 related examples for each chemical component.
	related_mapping_method:  `Literal`
		The method used to establish the resource correspondence.
	resource_accession_code:  `str`
		The resource identifier code for the related chemical reference.
	resource_name:  `Literal`
		The resource name for the related chemical reference.

	"""
	comp_id: str
	ordinal: int
	related_mapping_method: Literal["assigned by DrugBank resource", "assigned by PDB", "assigned by PubChem resource", "matching ChEMBL ID in Pharos", "matching InChIKey in DrugBank", "matching InChIKey in PubChem", "matching InChIKey-prefix in DrugBank", "matching by RESID resource"] | None = None
	resource_accession_code: str | None = None
	resource_name: Literal["CAS", "CCDC/CSD", "COD", "ChEBI", "ChEMBL", "DrugBank", "Pharos", "PubChem", "RESID"] | None = None
