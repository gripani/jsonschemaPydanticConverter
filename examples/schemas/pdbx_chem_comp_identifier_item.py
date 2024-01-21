from typing import Literal

from pydantic import BaseModel


class PdbxChemCompIdentifierItem(BaseModel):
	"""
	PdbxChemCompIdentifierItem class

	Attributes
	----------
	comp_id:  `str`
		This data item is a pointer to _chem_comp.id in the CHEM_COMP
		 category.
	identifier:  `str`
		This data item contains the identifier value for this
		 component.
	program:  `str`
		This data item contains the name of the program
		 or library used to compute the identifier.
	program_version:  `str`
		This data item contains the version of the program
		 or library used to compute the identifier.
	type:  `Literal`
		This data item contains the identifier type.

	"""
	comp_id: str
	identifier: str | None = None
	program: str
	program_version: str
	type: Literal["CAS REGISTRY NUMBER", "COMMON NAME", "CONDENSED IUPAC CARB SYMBOL", "CONDENSED IUPAC CARBOHYDRATE SYMBOL", "IUPAC CARB SYMBOL", "IUPAC CARBOHYDRATE SYMBOL", "MDL Identifier", "PUBCHEM Identifier", "SNFG CARB SYMBOL", "SNFG CARBOHYDRATE SYMBOL", "SYNONYM", "SYSTEMATIC NAME"]
