from typing import List

from pydantic import BaseModel


class RcsbBirdCitationItem(BaseModel):
	"""
	RcsbBirdCitationItem class

	Attributes
	----------
	id:  `str`
		The value of _rcsb_bird_citation.id must uniquely identify a record in the
		 rcsb_bird_citation list.
	journal_abbrev:  `str`
		Abbreviated name of the cited journal as given in the
		 Chemical Abstracts Service Source Index.
	journal_volume:  `str`
		Volume number of the journal cited; relevant for journal
		 articles.
	page_first:  `str`
		The first page of the rcsb_bird_citation; relevant for journal
		 articles, books and book chapters.
	page_last:  `str`
		The last page of the rcsb_bird_citation; relevant for journal
		 articles, books and book chapters.
	pdbx_database_id_DOI:  `str`
		Document Object Identifier used by doi.org to uniquely
		 specify bibliographic entry.
	pdbx_database_id_PubMed:  `int`
		Ascession number used by PubMed to categorize a specific
		 bibliographic entry.
	rcsb_authors:  `List`

	title:  `str`
		The title of the rcsb_bird_citation; relevant for journal articles, books
		 and book chapters.
	year:  `int`
		The year of the rcsb_bird_citation; relevant for journal articles, books
		 and book chapters.

	"""
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
