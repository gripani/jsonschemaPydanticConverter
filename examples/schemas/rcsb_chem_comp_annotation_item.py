from typing import List, Literal

from pydantic import BaseModel

from examples.schemas.annotation_lineage_item import AnnotationLineageItem


class RcsbChemCompAnnotationItem(BaseModel):
	"""
	RcsbChemCompAnnotationItem class

	Attributes
	----------
	annotation_id:  `str`
		An identifier for the annotation.
	assignment_version:  `str`
		Identifies the version of the annotation assignment.
	description:  `str`
		A description for the annotation.
	name:  `str`
		A name for the annotation.
	provenance_source:  `str`
		Code identifying the individual, organization or program that
		 assigned the annotation.
	type:  `Literal`
		A type or category of the annotation.
	annotation_lineage:  `List`


	"""
	annotation_id: str | None = None
	assignment_version: str | None = None
	description: str | None = None
	name: str | None = None
	provenance_source: str | None = None
	type: Literal["ATC", "Carbohydrate Anomer", "Carbohydrate Isomer", "Carbohydrate Primary Carbonyl Group", "Carbohydrate Ring", "Generating Enzyme", "Modification Type", "PSI-MOD"] | None = None
	annotation_lineage: List[AnnotationLineageItem] | None = None
