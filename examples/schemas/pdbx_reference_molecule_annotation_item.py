from pydantic import BaseModel


class PdbxReferenceMoleculeAnnotationItem(BaseModel):
	"""
	PdbxReferenceMoleculeAnnotationItem class

	Attributes
	----------
	family_prd_id:  `str`
		The value of _pdbx_reference_molecule_annotation.family_prd_id is a reference to
		 _pdbx_reference_molecule_list.family_prd_id in category PDBX_REFERENCE_MOLECULE_FAMILY_LIST.
	ordinal:  `int`
		This data item distinguishes anotations for this entity.
	prd_id:  `str`
		This data item is a pointer to _pdbx_reference_molecule.prd_id in the
		 PDB_REFERENCE_MOLECULE category.
	source:  `str`
		The source of the annoation for this entity.
	text:  `str`
		Text describing the annotation for this entity.
	type:  `str`
		Type of annotation for this entity.

	"""
	family_prd_id: str
	ordinal: int
	prd_id: str | None = None
	source: str | None = None
	text: str | None = None
	type: str | None = None
