from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntityPolyItem(BaseModel):
	"""
	PdbxReferenceEntityPolyItem class

	Attributes
	----------
	db_code:  `str`
		The database code for this source information
	db_name:  `str`
		The database name for this source information
	prd_id:  `str`
		The value of _pdbx_reference_entity_poly.prd_id is a reference
			       _pdbx_reference_entity_list.prd_id in the  PDBX_REFERENCE_ENTITY_LIST category.
	ref_entity_id:  `str`
		The value of _pdbx_reference_entity_poly.ref_entity_id is a reference
		 to _pdbx_reference_entity_list.ref_entity_id in PDBX_REFERENCE_ENTITY_LIST category.
	type:  `Literal`
		The type of the polymer.

	"""
	db_code: str | None = None
	db_name: str | None = None
	prd_id: str
	ref_entity_id: str
	type: Literal["nucleic-acid-like", "oligosaccharide", "peptide-like", "polysaccharide-like"] | None = None
