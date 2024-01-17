from pydantic import BaseModel


class RcsbChemCompDescriptor(BaseModel):

	InChI: str | None = None
	InChIKey: str | None = None
	SMILES: str | None = None
	SMILES_stereo: str | None = None
	comp_id: str
