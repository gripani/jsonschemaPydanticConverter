from typing import List, Literal

from pydantic import BaseModel


class RcsbChemCompTargetItem(BaseModel):
	"""
	RcsbChemCompTargetItem class

	Attributes
	----------
	comp_id:  `str`
		The value of _rcsb_chem_comp_target.comp_id is a reference to
		 a chemical component definition.
	interaction_type:  `str`
		The type of target interaction.
	name:  `str`
		The chemical component target name.
	ordinal:  `int`
		The value of _rcsb_chem_comp_target.ordinal distinguishes
		 related examples for each chemical component.
	provenance_source:  `Literal`
		A code indicating the provenance of the target interaction assignment
	reference_database_accession_code:  `str`
		The reference identifier code for the target interaction reference.
	reference_database_name:  `Literal`
		The reference database name for the target interaction.
	target_actions:  `List`


	"""
	comp_id: str
	interaction_type: str | None = None
	name: str | None = None
	ordinal: int
	provenance_source: Literal["DrugBank", "PDB Primary Data"] | None = None
	reference_database_accession_code: str | None = None
	reference_database_name: Literal["UniProt"] | None = None
	target_actions: List[str] | None = None
