from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntityListItem(BaseModel):
	"""
	PdbxReferenceEntityListItem class

	Attributes
	----------
	component_id:  `int`
		The component number of this entity within the molecule.
	details:  `str`
		Additional details about this entity.
	prd_id:  `str`
		The value of _pdbx_reference_entity_list.prd_id is a reference
		 _pdbx_reference_molecule.prd_id in the PDBX_REFERENCE_MOLECULE category.
	ref_entity_id:  `str`
		The value of _pdbx_reference_entity_list.ref_entity_id is a unique identifier
		 the a constituent entity within this reference molecule.
	type:  `Literal`
		Defines the polymer characteristic of the entity.

	"""
	component_id: int
	details: str | None = None
	prd_id: str
	ref_entity_id: str
	type: Literal["branched", "non-polymer", "polymer", "polymer-like"] | None = None
