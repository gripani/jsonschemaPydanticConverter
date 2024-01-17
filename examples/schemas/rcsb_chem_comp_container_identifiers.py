from typing import List

from pydantic import BaseModel


class RcsbChemCompContainerIdentifiers(BaseModel):

	atc_codes: List[str] | None = None
	comp_id: str
	drugbank_id: str | None = None
	prd_id: str | None = None
	rcsb_id: str | None = None
	subcomponent_ids: List[str] | None = None
