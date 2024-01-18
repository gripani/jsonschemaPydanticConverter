from pydantic import BaseModel


class PdbxReferenceMoleculeFeaturesItem(BaseModel):
	"""
	PdbxReferenceMoleculeFeaturesItem class

	Attributes
	----------
	family_prd_id:  `str`
		The value of _pdbx_reference_molecule_features.family_prd_id is a reference to
		 _pdbx_reference_molecule_list.family_prd_id in category PDBX_REFERENCE_MOLECULE_FAMILY_LIST.
	ordinal:  `int`
		The value of _pdbx_reference_molecule_features.ordinal distinguishes
			       each feature for this entity.
	prd_id:  `str`
		The value of _pdbx_reference_molecule_features.prd_id is a reference
			       _pdbx_reference_molecule.prd_id in the  PDBX_REFERENCE_MOLECULE category.
	source:  `str`
		The information source for the component feature.
	source_ordinal:  `int`
		The value of _pdbx_reference_molecule_features.source_ordinal provides
			       the priority order of features from a particular source or database.
	type:  `str`
		The entity feature type.
	value:  `str`
		The entity feature value.

	"""
	family_prd_id: str
	ordinal: int
	prd_id: str
	source: str | None = None
	source_ordinal: int | None = None
	type: str | None = None
	value: str | None = None
