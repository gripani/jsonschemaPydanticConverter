from typing import List, Literal

from pydantic import BaseModel


class ChemComp(BaseModel):

	formula: str | None = None
	formula_weight: float | None = None
	id: str
	mon_nstd_parent_comp_id: List[str] | None = None
	name: str | None = None
	one_letter_code: str | None = None
	pdbx_ambiguous_flag: str | None = None
	pdbx_formal_charge: int | None = None
	pdbx_initial_date: str | None = None
	pdbx_modified_date: str | None = None
	pdbx_processing_site: Literal["EBI", "PDBC", "PDBE", "PDBJ", "RCSB"] | None = None
	pdbx_release_status: Literal["DEL", "HOLD", "HPUB", "OBS", "REF_ONLY", "REL"] | None = None
	pdbx_replaced_by: str | None = None
	pdbx_replaces: str | None = None
	pdbx_subcomponent_list: str | None = None
	three_letter_code: str | None = None
	type: Literal["D-beta-peptide, C-gamma linking", "D-gamma-peptide, C-delta linking", "D-peptide COOH carboxy terminus", "D-peptide NH3 amino terminus", "D-peptide linking", "D-saccharide", "D-saccharide, alpha linking", "D-saccharide, beta linking", "DNA OH 3 prime terminus", "DNA OH 5 prime terminus", "DNA linking", "L-DNA linking", "L-RNA linking", "L-beta-peptide, C-gamma linking", "L-gamma-peptide, C-delta linking", "L-peptide COOH carboxy terminus", "L-peptide NH3 amino terminus", "L-peptide linking", "L-saccharide", "L-saccharide, alpha linking", "L-saccharide, beta linking", "RNA OH 3 prime terminus", "RNA OH 5 prime terminus", "RNA linking", "non-polymer", "other", "peptide linking", "peptide-like", "saccharide"] | None = None
