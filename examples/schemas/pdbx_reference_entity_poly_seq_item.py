from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntityPolySeqItem(BaseModel):
	"""
	PdbxReferenceEntityPolySeqItem class

	Attributes
	----------
	hetero:  `Literal`
		A flag to indicate that sequence heterogeneity at this monomer position.
	mon_id:  `str`
		This data item is the chemical component identifier of monomer.
	num:  `int`
		The value of _pdbx_reference_entity_poly_seq.num must uniquely and sequentially
		 identify a record in the PDBX_REFERENCE_ENTITY_POLY_SEQ list.
		
		 This value is conforms to author numbering conventions and does not map directly
		 to the numbering conventions used for _entity_poly_seq.num.
	observed:  `Literal`
		A flag to indicate that this monomer is observed in the instance example.
	parent_mon_id:  `str`
		This data item is the chemical component identifier for the parent component corresponding to this monomer.
	prd_id:  `str`
		The value of _pdbx_reference_entity_poly_seq.prd_id is a reference
			       _pdbx_reference_entity_poly.prd_id in the  PDBX_REFERENCE_ENTITY_POLY category.
	ref_entity_id:  `str`
		The value of _pdbx_reference_entity_poly_seq.ref_entity_id is a reference
		 to _pdbx_reference_entity_poly.ref_entity_id in PDBX_REFERENCE_ENTITY_POLY category.

	"""
	hetero: Literal["N", "Y"]
	mon_id: str
	num: int
	observed: Literal["N", "Y"] | None = None
	parent_mon_id: str | None = None
	prd_id: str
	ref_entity_id: str
