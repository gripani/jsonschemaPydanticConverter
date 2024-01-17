from typing import Literal

from pydantic import BaseModel


class PdbxFamilyPrdAuditItem(BaseModel):

	action_type: Literal["Add PRD", "Create family", "Initial release", "Modify annotation", "Modify citation", "Modify family classification", "Modify family name", "Modify feature", "Modify molecule details", "Modify related structures", "Modify sequence", "Modify synonyms", "Obsolete family", "Obsolete familyt", "Other modification", "Remove PRD"]
	annotator: str | None = None
	date: str
	details: str | None = None
	family_prd_id: str
	processing_site: str | None = None
