from typing import Literal

from pydantic import BaseModel


class PdbxReferenceMolecule(BaseModel):
	"""
	PdbxReferenceMolecule class

	Attributes
	----------
	chem_comp_id:  `str`
		For entities represented as single molecules, the identifier
		 corresponding to the chemical definition for the molecule.
	_class:  `Literal`
		Broadly defines the function of the entity.
	class_evidence_code:  `str`
		Evidence for the assignment of _pdbx_reference_molecule.class
	compound_details:  `str`
		Special details about this molecule.
	description:  `str`
		Description of this molecule.
	formula:  `str`
		The formula for the reference entity. Formulae are written
		 according to the rules:
		
		 1. Only recognised element symbols may be used.
		
		 2. Each element symbol is followed by a 'count' number. A count
		    of '1' may be omitted.
		
		 3. A space or parenthesis must separate each element symbol and
		    its count, but in general parentheses are not used.
		
		 4. The order of elements depends on whether or not carbon is
		    present. If carbon is present, the order should be: C, then
		    H, then the other elements in alphabetical order of their
		    symbol. If carbon is not present, the elements are listed
		    purely in alphabetic order of their symbol. This is the
		    'Hill' system used by Chemical Abstracts.
	formula_weight:  `float`
		Formula mass in daltons of the entity.
	name:  `str`
		A name of the entity.
	prd_id:  `str`
		The value of _pdbx_reference_molecule.prd_id is the unique identifier
		 for the reference molecule in this family.
		
		 By convention this ID uniquely identifies the reference molecule in
		 in the PDB reference dictionary.
		
		 The ID has the template form PRD_dddddd (e.g. PRD_000001)
	release_status:  `Literal`
		Defines the current PDB release status for this molecule definition.
	replaced_by:  `str`
		Assigns the identifier of the reference molecule that has replaced this molecule.
	replaces:  `str`
		Assigns the identifier for the reference molecule which have been replaced
		 by this reference molecule.
		 Multiple molecule identifier codes should be separated by commas.
	represent_as:  `Literal`
		Defines how this entity is represented in PDB data files.
	representative_PDB_id_code:  `str`
		The PDB accession code for the entry containing a representative example of this molecule.
	type:  `Literal`
		Defines the structural classification of the entity.
	type_evidence_code:  `str`
		Evidence for the assignment of _pdbx_reference_molecule.type

	"""
	chem_comp_id: str | None = None
	_class: Literal["Antagonist", "Anthelmintic", "Antibiotic", "Antibiotic, Anthelmintic", "Antibiotic, Antimicrobial", "Antibiotic, Antineoplastic", "Anticancer", "Anticoagulant", "Anticoagulant, Antithrombotic", "Antifungal", "Antigen", "Antiinflammatory", "Antimicrobial", "Antimicrobial, Antiparasitic, Antibiotic", "Antimicrobial, Antiretroviral", "Antimicrobial, Antitumor", "Antineoplastic", "Antiparasitic", "Antiretroviral", "Antithrombotic", "Antitumor", "Antiviral", "CASPASE inhibitor", "Chaperone binding", "Drug delivery", "Enzyme inhibitor", "Glycan component", "Growth factor", "Immunosuppressant", "Inducer", "Inhibitor", "Lantibiotic", "Metabolism", "Metal transport", "Nutrient", "Oxidation-reduction", "Protein binding", "Receptor", "Substrate analog", "Synthetic opioid", "Thrombin inhibitor", "Thrombin inhibitor, Trypsin inhibitor", "Toxin", "Transition state mimetic", "Transport activator", "Trypsin inhibitor", "Unknown", "Water retention"] | None = None
	class_evidence_code: str | None = None
	compound_details: str | None = None
	description: str | None = None
	formula: str | None = None
	formula_weight: float | None = None
	name: str | None = None
	prd_id: str
	release_status: Literal["HOLD", "OBS", "REL", "WAIT"] | None = None
	replaced_by: str | None = None
	replaces: str | None = None
	represent_as: Literal["branched", "polymer", "single molecule"] | None = None
	representative_PDB_id_code: str | None = None
	type: Literal["Amino acid", "Aminoglycoside", "Ansamycin", "Anthracycline", "Anthraquinone", "Chalkophore", "Chalkophore, Polypeptide", "Chromophore", "Cyclic depsipeptide", "Cyclic lipopeptide", "Cyclic peptide", "Glycopeptide", "Heterocyclic", "Imino sugar", "Keto acid", "Lipoglycopeptide", "Lipopeptide", "Macrolide", "Non-polymer", "Nucleoside", "Oligopeptide", "Oligosaccharide", "Peptaibol", "Peptide-like", "Polycyclic", "Polypeptide", "Polysaccharide", "Quinolone", "Siderophore", "Thiolactone", "Thiopeptide", "Unknown"] | None = None
	type_evidence_code: str | None = None
