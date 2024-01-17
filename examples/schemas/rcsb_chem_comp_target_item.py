from typing import List, Literal

from pydantic import BaseModel


class RcsbChemCompTargetItem(BaseModel):

	comp_id: str
	interaction_type: str | None = None
	name: str | None = None
	ordinal: int
	provenance_source: Literal["DrugBank", "PDB Primary Data"] | None = None
	reference_database_accession_code: str | None = None
	reference_database_name: Literal["UniProt"] | None = None
	target_actions: List[str] | None = None
