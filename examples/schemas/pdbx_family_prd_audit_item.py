from typing import Literal

from pydantic import BaseModel


class PdbxFamilyPrdAuditItem(BaseModel):
	"""
	PdbxFamilyPrdAuditItem class

	Attributes
	----------
	action_type:  `Literal`
		The action associated with this audit record.
	annotator:  `str`
		The initials of the annotator creating of modifying the family.
	date:  `str`
		The date associated with this audit record.
	details:  `str`
		Additional details decribing this change.
	family_prd_id:  `str`
		This data item is a pointer to _pdbx_reference_molecule_family.family_prd_id in the
			       pdbx_reference_molecule category.
	processing_site:  `str`
		An identifier for the wwPDB site creating or modifying the family.

	"""
	action_type: Literal["Add PRD", "Create family", "Initial release", "Modify annotation", "Modify citation", "Modify family classification", "Modify family name", "Modify feature", "Modify molecule details", "Modify related structures", "Modify sequence", "Modify synonyms", "Obsolete family", "Obsolete familyt", "Other modification", "Remove PRD"]
	annotator: str | None = None
	date: str
	details: str | None = None
	family_prd_id: str
	processing_site: str | None = None
