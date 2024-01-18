from pydantic import BaseModel


class PdbxReferenceMoleculeSynonymsItem(BaseModel):
	"""
	PdbxReferenceMoleculeSynonymsItem class

	Attributes
	----------
	family_prd_id:  `str`
		The value of _pdbx_reference_molecule_synonyms.family_prd_id is a reference to
		 _pdbx_reference_molecule_list.family_prd_id in category PDBX_REFERENCE_MOLECULE_FAMILY_LIST.
	name:  `str`
		A synonym name for the entity.
	ordinal:  `int`
		The value of _pdbx_reference_molecule_synonyms.ordinal is an ordinal
			       to distinguish synonyms for this entity.
	prd_id:  `str`
		The value of _pdbx_reference_molecule_synonyms.prd_id is a reference
			       _pdbx_reference_molecule.prd_id in the  PDBX_REFERENCE_MOLECULE category.
	source:  `str`
		The source of this synonym name for the entity.

	"""
	family_prd_id: str
	name: str | None = None
	ordinal: int
	prd_id: str
	source: str | None = None
