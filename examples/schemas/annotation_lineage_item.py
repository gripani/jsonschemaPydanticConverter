from pydantic import BaseModel


class AnnotationLineageItem(BaseModel):
	"""
	AnnotationLineageItem class

	Attributes
	----------
	depth:  `int`
		Members of the annotation lineage as parent lineage depth (1-N)
	id:  `str`
		Members of the annotation lineage as parent class identifiers.
	name:  `str`
		Members of the annotation lineage as parent class names.

	"""
	depth: int | None = None
	id: str | None = None
	name: str | None = None
