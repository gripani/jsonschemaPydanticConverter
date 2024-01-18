from typing import Literal

from pydantic import BaseModel


class PdbxReferenceEntitySequenceItem(BaseModel):
	"""
	PdbxReferenceEntitySequenceItem class

	Attributes
	----------
	NRP_flag:  `Literal`
		A flag to indicate a non-ribosomal entity.
	one_letter_codes:  `str`
		The one-letter-code sequence for this entity.  Non-standard monomers are represented as 'X'.
	prd_id:  `str`
		The value of _pdbx_reference_entity_sequence.prd_id is a reference
			       _pdbx_reference_entity_list.prd_id in the  PDBX_REFERENCE_ENTITY_LIST category.
	ref_entity_id:  `str`
		The value of _pdbx_reference_entity_sequence.ref_entity_id is a reference
		 to _pdbx_reference_entity_list.ref_entity_id in PDBX_REFERENCE_ENTITY_LIST category.
	type:  `Literal`
		The monomer type for the sequence.

	"""
	NRP_flag: Literal["N", "Y"] | None = None
	one_letter_codes: str | None = None
	prd_id: str
	ref_entity_id: str
	type: Literal["peptide-like", "saccharide"] | None = None
