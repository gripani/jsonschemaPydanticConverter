from typing import Literal

from pydantic import BaseModel


class PdbxReferenceMoleculeFamily(BaseModel):

	family_prd_id: str
	name: str | None = None
	release_status: Literal["HOLD", "OBS", "REL", "WAIT"] | None = None
	replaced_by: str | None = None
	replaces: str | None = None
