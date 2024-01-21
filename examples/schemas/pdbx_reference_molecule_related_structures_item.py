from pydantic import BaseModel


class PdbxReferenceMoleculeRelatedStructuresItem(BaseModel):
	"""
	PdbxReferenceMoleculeRelatedStructuresItem class

	Attributes
	----------
	citation_id:  `str`
		A link to related reference information in the citation category.
	db_accession:  `str`
		The database accession code for the related structure reference.
	db_code:  `str`
		The database identifier code for the related structure reference.
	db_name:  `str`
		The database name for the related structure reference.
	family_prd_id:  `str`
		The value of _pdbx_reference_molecule_related_structures.family_prd_id is a reference to
		 _pdbx_reference_molecule_list.family_prd_id in category PDBX_REFERENCE_MOLECULE_FAMILY_LIST.
	formula:  `str`
		The formula for the reference entity. Formulae are written
		 according to the rules:
		
		 1. Only recognised element symbols may be used.
		
		 2. Each element symbol is followed by a 'count' number. A count
		    of '1' may be omitted.
		
		 3. A space or parenthesis must separate each element symbol and
		    its count, but in general parentheses are not used.
		
		 4. The order of elements depends on whether or not carbon is
		    present. If carbon is present, the order should be: C, then
		    H, then the other elements in alphabetical order of their
		    symbol. If carbon is not present, the elements are listed
		    purely in alphabetic order of their symbol. This is the
		    'Hill' system used by Chemical Abstracts.
	name:  `str`
		The chemical name for the structure entry in the related database
	ordinal:  `int`
		The value of _pdbx_reference_molecule_related_structures.ordinal distinguishes
		 related structural data for each entity.

	"""
	citation_id: str | None = None
	db_accession: str | None = None
	db_code: str | None = None
	db_name: str | None = None
	family_prd_id: str
	formula: str | None = None
	name: str | None = None
	ordinal: int
