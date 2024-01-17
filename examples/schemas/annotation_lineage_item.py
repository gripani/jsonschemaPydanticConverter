from pydantic import BaseModel


class AnnotationLineageItem(BaseModel):

	depth: int | None = None
	id: str | None = None
	name: str | None = None
