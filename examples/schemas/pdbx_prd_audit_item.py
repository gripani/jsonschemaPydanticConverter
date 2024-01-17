from typing import Literal

from pydantic import BaseModel


class PdbxPrdAuditItem(BaseModel):

	action_type: Literal["Create molecule", "Initial release", "Modify audit", "Modify class", "Modify linkage", "Modify molecule name", "Modify representation", "Modify sequence", "Modify taxonomy organism", "Modify type", "Obsolete molecule", "Other modification"]
	annotator: str | None = None
	date: str
	details: str | None = None
	prd_id: str
	processing_site: Literal["BMRB", "PDBC", "PDBE", "PDBJ", "RCSB"] | None = None
