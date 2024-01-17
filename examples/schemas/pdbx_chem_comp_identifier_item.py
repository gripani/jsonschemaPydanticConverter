from typing import Literal

from pydantic import BaseModel


class PdbxChemCompIdentifierItem(BaseModel):

	comp_id: str
	identifier: str | None = None
	program: str
	program_version: str
	type: Literal["CAS REGISTRY NUMBER", "COMMON NAME", "CONDENSED IUPAC CARB SYMBOL", "CONDENSED IUPAC CARBOHYDRATE SYMBOL", "IUPAC CARB SYMBOL", "IUPAC CARBOHYDRATE SYMBOL", "MDL Identifier", "PUBCHEM Identifier", "SNFG CARB SYMBOL", "SNFG CARBOHYDRATE SYMBOL", "SYNONYM", "SYSTEMATIC NAME"]
