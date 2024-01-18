from pydantic import BaseModel


class PdbxReferenceMoleculeListItem(BaseModel):
	"""
	PdbxReferenceMoleculeListItem class

	Attributes
	----------
	family_prd_id:  `str`
		The value of _pdbx_reference_molecule_list.family_prd_id is a reference to
		 _pdbx_reference_molecule_family.family_prd_id' in category PDBX_REFERENCE_MOLECULE_FAMILY.
	prd_id:  `str`
		The value of _pdbx_reference_molecule_list.prd_id is the unique identifier
		 for the reference molecule in this family.
		
		 By convention this ID uniquely identifies the reference molecule in
		 in the PDB reference dictionary.
		
		 The ID has the template form PRD_dddddd (e.g. PRD_000001)

	"""
	family_prd_id: str
	prd_id: str
