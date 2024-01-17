from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntityListItem(BaseModel):

	component_id: int
	details: str | None = None
	prd_id: str
	ref_entity_id: str
	type: Literal["branched", "non-polymer", "polymer", "polymer-like"] | None = None
