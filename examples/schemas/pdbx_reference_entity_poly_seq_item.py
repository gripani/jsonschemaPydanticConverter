from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntityPolySeqItem(BaseModel):

	hetero: Literal["N", "Y"]
	mon_id: str
	num: int
	observed: Literal["N", "Y"] | None = None
	parent_mon_id: str | None = None
	prd_id: str
	ref_entity_id: str
