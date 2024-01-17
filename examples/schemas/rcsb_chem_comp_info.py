from typing import Literal

from pydantic import BaseModel


class RcsbChemCompInfo(BaseModel):

	atom_count: int | None = None
	atom_count_chiral: int | None = None
	atom_count_heavy: int | None = None
	bond_count: int | None = None
	bond_count_aromatic: int | None = None
	comp_id: str
	initial_deposition_date: str | None = None
	initial_release_date: str | None = None
	release_status: Literal["DEL", "HOLD", "HPUB", "OBS", "REF_ONLY", "REL"] | None = None
	revision_date: str | None = None
