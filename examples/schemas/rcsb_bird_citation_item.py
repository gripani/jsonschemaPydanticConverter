from typing import List

from pydantic import BaseModel


class RcsbBirdCitationItem(BaseModel):

	id: str
	journal_abbrev: str | None = None
	journal_volume: str | None = None
	page_first: str | None = None
	page_last: str | None = None
	pdbx_database_id_DOI: str | None = None
	pdbx_database_id_PubMed: int | None = None
	rcsb_authors: List[str] | None = None
	title: str | None = None
	year: int | None = None
