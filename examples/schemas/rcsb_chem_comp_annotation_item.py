from typing import List, Literal

from pydantic import BaseModel

from examples.schemas.annotation_lineage_item import AnnotationLineageItem


class RcsbChemCompAnnotationItem(BaseModel):

	annotation_id: str | None = None
	assignment_version: str | None = None
	description: str | None = None
	name: str | None = None
	provenance_source: str | None = None
	type: Literal["ATC", "Carbohydrate Anomer", "Carbohydrate Isomer", "Carbohydrate Primary Carbonyl Group", "Carbohydrate Ring", "Generating Enzyme", "Modification Type", "PSI-MOD"] | None = None
	annotation_lineage: List[AnnotationLineageItem] | None = None
