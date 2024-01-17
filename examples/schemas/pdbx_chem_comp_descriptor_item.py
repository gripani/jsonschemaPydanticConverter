from typing import Literal

from pydantic import BaseModel


class PdbxChemCompDescriptorItem(BaseModel):

	comp_id: str
	descriptor: str | None = None
	program: str
	program_version: str
	type: Literal["InChI", "InChIKey", "InChI_CHARGE", "InChI_FIXEDH", "InChI_ISOTOPE", "InChI_MAIN", "InChI_MAIN_CONNECT", "InChI_MAIN_FORMULA", "InChI_MAIN_HATOM", "InChI_RECONNECT", "InChI_STEREO", "SMILES", "SMILES_CANNONICAL", "SMILES_CANONICAL"]
