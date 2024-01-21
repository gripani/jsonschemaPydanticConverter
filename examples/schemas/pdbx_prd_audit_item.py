from typing import Literal

from pydantic import BaseModel


class PdbxPrdAuditItem(BaseModel):
	"""
	PdbxPrdAuditItem class

	Attributes
	----------
	action_type:  `Literal`
		The action associated with this audit record.
	annotator:  `str`
		The initials of the annotator creating of modifying the molecule.
	date:  `str`
		The date associated with this audit record.
	details:  `str`
		Additional details decribing this change.
	prd_id:  `str`
		This data item is a pointer to _pdbx_reference_molecule.prd_id in the
			       pdbx_reference_molecule category.
	processing_site:  `Literal`
		An identifier for the wwPDB site creating or modifying the molecule.

	"""
	action_type: Literal["Create molecule", "Initial release", "Modify audit", "Modify class", "Modify linkage", "Modify molecule name", "Modify representation", "Modify sequence", "Modify taxonomy organism", "Modify type", "Obsolete molecule", "Other modification"]
	annotator: str | None = None
	date: str
	details: str | None = None
	prd_id: str
	processing_site: Literal["BMRB", "PDBC", "PDBE", "PDBJ", "RCSB"] | None = None
