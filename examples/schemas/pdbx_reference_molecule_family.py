from typing import Literal

from pydantic import BaseModel


class PdbxReferenceMoleculeFamily(BaseModel):
	"""
	PdbxReferenceMoleculeFamily class

	Attributes
	----------
	family_prd_id:  `str`
		The value of _pdbx_reference_entity.family_prd_id must uniquely identify a record in the
		 PDBX_REFERENCE_MOLECULE_FAMILY list.
		
		 By convention this ID uniquely identifies the reference family in
		 in the PDB reference dictionary.
		
		 The ID has the template form FAM_dddddd (e.g. FAM_000001)
	name:  `str`
		The entity family name.
	release_status:  `Literal`
		Assigns the current PDB release status for this family.
	replaced_by:  `str`
		Assigns the identifier of the family that has replaced this component.
	replaces:  `str`
		Assigns the identifier for the family which have been replaced by this family.
		 Multiple family identifier codes should be separated by commas.

	"""
	family_prd_id: str
	name: str | None = None
	release_status: Literal["HOLD", "OBS", "REL", "WAIT"] | None = None
	replaced_by: str | None = None
	replaces: str | None = None
