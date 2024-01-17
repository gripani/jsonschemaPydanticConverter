from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntitySequenceItem(BaseModel):

	NRP_flag: Literal["N", "Y"] | None = None
	one_letter_codes: str | None = None
	prd_id: str
	ref_entity_id: str
	type: Literal["peptide-like", "saccharide"] | None = None
