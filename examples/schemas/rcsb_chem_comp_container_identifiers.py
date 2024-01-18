from typing import List

from pydantic import BaseModel


class RcsbChemCompContainerIdentifiers(BaseModel):
	"""
	RcsbChemCompContainerIdentifiers class

	Attributes
	----------
	atc_codes:  `List`

	comp_id:  `str`
		The chemical component identifier.
	drugbank_id:  `str`
		The DrugBank identifier corresponding to the chemical component.
	prd_id:  `str`
		The BIRD definition identifier.
	rcsb_id:  `str`
		A unique identifier for the chemical definition in this container.
	subcomponent_ids:  `List`


	"""
	atc_codes: List[str] | None = None
	comp_id: str
	drugbank_id: str | None = None
	prd_id: str | None = None
	rcsb_id: str | None = None
	subcomponent_ids: List[str] | None = None
