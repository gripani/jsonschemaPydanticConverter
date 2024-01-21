from typing import Literal

from pydantic import BaseModel


class RcsbChemCompInfo(BaseModel):
	"""
	RcsbChemCompInfo class

	Attributes
	----------
	atom_count:  `int`
		Chemical component total atom count
	atom_count_chiral:  `int`
		Chemical component chiral atom count
	atom_count_heavy:  `int`
		Chemical component heavy atom count
	bond_count:  `int`
		Chemical component total bond count
	bond_count_aromatic:  `int`
		Chemical component aromatic bond count
	comp_id:  `str`
		The chemical component identifier.
	initial_deposition_date:  `str`
		The date the chemical definition was first deposited in the PDB repository.
	initial_release_date:  `str`
		The initial date the chemical definition was released in the PDB repository.
	release_status:  `Literal`
		The release status of the chemical definition.
	revision_date:  `str`
		The date of last revision of the chemical definition.

	"""
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
