from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntityPolyLinkItem(BaseModel):
	"""
	PdbxReferenceEntityPolyLinkItem class

	Attributes
	----------
	atom_id_1:  `str`
		The atom identifier/name in the first of the two components making
		 the linkage.
	atom_id_2:  `str`
		The atom identifier/name in the second of the two components making
		 the linkage.
	comp_id_1:  `str`
		The component identifier in the first of the two components making the
		 linkage.
		
		 This data item is a pointer to _pdbx_reference_entity_poly_seq.mon_id
		 in the PDBX_REFERENCE_ENTITY_POLY_SEQ category.
	comp_id_2:  `str`
		The component identifier in the second of the two components making the
		 linkage.
		
		 This data item is a pointer to _pdbx_reference_entity_poly_seq.mon_id
		 in the PDBX_REFERENCE_ENTITY_POLY_SEQ category.
	component_id:  `int`
		The entity component identifier entity containing the linkage.
	entity_seq_num_1:  `int`
		For a polymer entity, the sequence number in the first of
		 the two components making the linkage.
		
		 This data item is a pointer to _pdbx_reference_entity_poly_seq.num
		 in the PDBX_REFERENCE_ENTITY_POLY_SEQ category.
	entity_seq_num_2:  `int`
		For a polymer entity, the sequence number in the second of
		 the two components making the linkage.
		
		 This data item is a pointer to _pdbx_reference_entity_poly_seq.num
		 in the PDBX_REFERENCE_ENTITY_POLY_SEQ category.
	link_id:  `int`
		The value of _pdbx_reference_entity_poly_link.link_id uniquely identifies
		 a linkage within a polymer entity.
	prd_id:  `str`
		The value of _pdbx_reference_entity_poly_link.prd_id is a reference
		 _pdbx_reference_entity_list.prd_id in the PDBX_REFERENCE_ENTITY_POLY category.
	ref_entity_id:  `str`
		The reference entity id of the polymer entity containing the linkage.
		
		 This data item is a pointer to _pdbx_reference_entity_poly.ref_entity_id
		 in the PDBX_REFERENCE_ENTITY_POLY category.
	value_order:  `Literal`
		The bond order target for the non-standard linkage.

	"""
	atom_id_1: str | None = None
	atom_id_2: str | None = None
	comp_id_1: str | None = None
	comp_id_2: str | None = None
	component_id: int
	entity_seq_num_1: int | None = None
	entity_seq_num_2: int | None = None
	link_id: int
	prd_id: str
	ref_entity_id: str
	value_order: Literal["arom", "delo", "doub", "pi", "poly", "quad", "sing", "trip"] | None = None
