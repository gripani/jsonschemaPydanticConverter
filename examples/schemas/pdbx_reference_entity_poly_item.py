from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntityPolyItem(BaseModel):

	db_code: str | None = None
	db_name: str | None = None
	prd_id: str
	ref_entity_id: str
	type: Literal["nucleic-acid-like", "oligosaccharide", "peptide-like", "polysaccharide-like"] | None = None
