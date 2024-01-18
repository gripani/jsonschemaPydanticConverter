from typing import List, Literal

from pydantic import BaseModel


class ChemComp(BaseModel):
	"""
	ChemComp class

	Attributes
	----------
	formula:  `str`
		The formula for the chemical component. Formulae are written
		 according to the following rules:
		
		 (1) Only recognized element symbols may be used.
		
		 (2) Each element symbol is followed by a 'count' number. A count
		    of '1' may be omitted.
		
		 (3) A space or parenthesis must separate each cluster of
		    (element symbol + count), but in general parentheses are
		    not used.
		
		 (4) The order of elements depends on whether carbon is
		    present or not. If carbon is present, the order should be:
		    C, then H, then the other elements in alphabetical order
		    of their symbol. If carbon is not present, the elements
		    are listed purely in alphabetic order of their symbol. This
		    is the 'Hill' system used by Chemical Abstracts.
	formula_weight:  `float`
		Formula mass of the chemical component.
	id:  `str`
		The value of _chem_comp.id must uniquely identify each item in
		 the CHEM_COMP list.
		
		 For protein polymer entities, this is the three-letter code for
		 the amino acid.
		
		 For nucleic acid polymer entities, this is the one-letter code
		 for the base.
	mon_nstd_parent_comp_id:  `List`

	name:  `str`
		The full name of the component.
	one_letter_code:  `str`
		For standard polymer components, the one-letter code for
		 the component.   For non-standard polymer components, the
		 one-letter code for parent component if this exists;
		 otherwise, the one-letter code should be given as 'X'.
		
		 Components that derived from multiple parents components
		 are described by a sequence of one-letter-codes.
	pdbx_ambiguous_flag:  `str`
		A preliminary classification used by PDB to indicate
		 that the chemistry of this component while described
		 as clearly as possible is still ambiguous.  Software
		 tools may not be able to process this component
		 definition.
	pdbx_formal_charge:  `int`
		The net integer charge assigned to this component. This is the
		 formal charge assignment normally found in chemical diagrams.
	pdbx_initial_date:  `str`
		Date component was added to database.
	pdbx_modified_date:  `str`
		Date component was last modified.
	pdbx_processing_site:  `Literal`
		This data item identifies the deposition site that processed
		 this chemical component defintion.
	pdbx_release_status:  `Literal`
		This data item holds the current release status for the component.
	pdbx_replaced_by:  `str`
		Identifies the _chem_comp.id of the component that
		 has replaced this component.
	pdbx_replaces:  `str`
		Identifies the _chem_comp.id's of the components
		 which have been replaced by this component.
		 Multiple id codes should be separated by commas.
	pdbx_subcomponent_list:  `str`
		The list of subcomponents contained in this component.
	three_letter_code:  `str`
		For standard polymer components, the common three-letter code for
		 the component.   Non-standard polymer components and non-polymer
		 components are also assigned three-letter-codes.
		
		 For ambiguous polymer components three-letter code should
		 be given as 'UNK'.  Ambiguous ions are assigned the code 'UNX'.
		 Ambiguous non-polymer components are assigned the code 'UNL'.
	type:  `Literal`
		For standard polymer components, the type of the monomer.
		 Note that monomers that will form polymers are of three types:
		 linking monomers, monomers with some type of N-terminal (or 5')
		 cap and monomers with some type of C-terminal (or 3') cap.

	"""
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
