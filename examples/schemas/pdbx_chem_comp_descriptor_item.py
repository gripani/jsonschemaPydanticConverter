from typing import Literal

from pydantic import BaseModel


class PdbxChemCompDescriptorItem(BaseModel):
	"""
	PdbxChemCompDescriptorItem class

	Attributes
	----------
	comp_id:  `str`
		This data item is a pointer to _chem_comp.id in the CHEM_COMP
		 category.
	descriptor:  `str`
		This data item contains the descriptor value for this
		 component.
	program:  `str`
		This data item contains the name of the program
		 or library used to compute the descriptor.
	program_version:  `str`
		This data item contains the version of the program
		 or library used to compute the descriptor.
	type:  `Literal`
		This data item contains the descriptor type.

	"""
	comp_id: str
	descriptor: str | None = None
	program: str
	program_version: str
	type: Literal["InChI", "InChIKey", "InChI_CHARGE", "InChI_FIXEDH", "InChI_ISOTOPE", "InChI_MAIN", "InChI_MAIN_CONNECT", "InChI_MAIN_FORMULA", "InChI_MAIN_HATOM", "InChI_RECONNECT", "InChI_STEREO", "SMILES", "SMILES_CANNONICAL", "SMILES_CANONICAL"]
