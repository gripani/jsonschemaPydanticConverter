from typing import Literal

from pydantic import BaseModel


class PdbxReferenceMolecule(BaseModel):

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
