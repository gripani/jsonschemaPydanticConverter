from typing import Literal

from pydantic import BaseModel


class PdbxChemCompAuditItem(BaseModel):

	action_type: Literal["Create component", "Initial release", "Modify aromatic_flag", "Modify atom id", "Modify backbone", "Modify charge", "Modify component atom id", "Modify component comp_id", "Modify coordinates", "Modify descriptor", "Modify formal charge", "Modify formula", "Modify identifier", "Modify internal type", "Modify leaving atom flag", "Modify linking type", "Modify model coordinates code", "Modify name", "Modify one letter code", "Modify parent residue", "Modify processing site", "Modify subcomponent list", "Modify synonyms", "Modify value order", "Obsolete component", "Other modification"] | None = None
	comp_id: str | None = None
	date: str | None = None
	details: str | None = None
	ordinal: int
