from typing import Literal

from pydantic import BaseModel


class PdbxChemCompFeatureItem(BaseModel):
	"""
	PdbxChemCompFeatureItem class

	Attributes
	----------
	comp_id:  `str`
		The component identifier for this feature.
	source:  `str`
		The information source for the component feature.
	type:  `Literal`
		The component feature type.
	value:  `str`
		The component feature value.

	"""
	comp_id: str
	source: str
	type: Literal["CARBOHYDRATE ANOMER", "CARBOHYDRATE ISOMER", "CARBOHYDRATE PRIMARY CARBONYL GROUP", "CARBOHYDRATE RING"]
	value: str
