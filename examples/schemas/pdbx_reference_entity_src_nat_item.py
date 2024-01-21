from pydantic import BaseModel


class PdbxReferenceEntitySrcNatItem(BaseModel):
	"""
	PdbxReferenceEntitySrcNatItem class

	Attributes
	----------
	atcc:  `str`
		The Americal Tissue Culture Collection code for organism from which the entity was isolated.
	db_code:  `str`
		The database code for this source information
	db_name:  `str`
		The database name for this source information
	ordinal:  `int`
		The value of _pdbx_reference_entity_src_nat.ordinal distinguishes
			       source details for this entity.
	organism_scientific:  `str`
		The scientific name of the organism from which the entity was isolated.
	prd_id:  `str`
		The value of _pdbx_reference_entity_src_nat.prd_id is a reference
			       _pdbx_reference_entity_list.prd_id in the  PDBX_REFERENCE_ENTITY_LIST category.
	ref_entity_id:  `str`
		The value of _pdbx_reference_entity_src_nat.ref_entity_id is a reference
		 to _pdbx_reference_entity_list.ref_entity_id in PDBX_REFERENCE_ENTITY_LIST category.
	source:  `str`
		The data source for this information.
	source_id:  `str`
		A identifier within the data source for this information.
	taxid:  `str`
		The NCBI TaxId of the organism from which the entity was isolated.

	"""
	atcc: str | None = None
	db_code: str | None = None
	db_name: str | None = None
	ordinal: int
	organism_scientific: str | None = None
	prd_id: str
	ref_entity_id: str
	source: str | None = None
	source_id: str | None = None
	taxid: str | None = None
