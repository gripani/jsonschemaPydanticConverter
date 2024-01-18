from pydantic import BaseModel


class PdbxReferenceMoleculeDetailsItem(BaseModel):
	"""
	PdbxReferenceMoleculeDetailsItem class

	Attributes
	----------
	family_prd_id:  `str`
		The value of _pdbx_reference_molecule_details.family_prd_id is a reference to
		 _pdbx_reference_molecule_list.family_prd_id' in category PDBX_REFERENCE_MOLECULE_FAMILY.
	ordinal:  `int`
		The value of _pdbx_reference_molecule_details.ordinal is an ordinal that
		 distinguishes each descriptive text for this entity.
	source:  `str`
		A data source of this information (e.g. PubMed, Merck Index)
	source_id:  `str`
		A identifier within the data source for this information.
	text:  `str`
		The text of the description of special aspects of the entity.

	"""
	family_prd_id: str
	ordinal: int
	source: str | None = None
	source_id: str | None = None
	text: str | None = None
