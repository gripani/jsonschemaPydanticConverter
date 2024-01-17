from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntityPolyLinkItem(BaseModel):

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
