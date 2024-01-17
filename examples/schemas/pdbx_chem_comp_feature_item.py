from typing import Literal

from pydantic import BaseModel


class PdbxChemCompFeatureItem(BaseModel):

	comp_id: str
	source: str
	type: Literal["CARBOHYDRATE ANOMER", "CARBOHYDRATE ISOMER", "CARBOHYDRATE PRIMARY CARBONYL GROUP", "CARBOHYDRATE RING"]
	value: str
