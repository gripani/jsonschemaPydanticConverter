from typing import List

from pydantic import BaseModel

from examples.schemas.chem_comp import ChemComp
from examples.schemas.pdbx_chem_comp_audit_item import PdbxChemCompAuditItem
from examples.schemas.pdbx_chem_comp_descriptor_item import PdbxChemCompDescriptorItem
from examples.schemas.pdbx_chem_comp_feature_item import PdbxChemCompFeatureItem
from examples.schemas.pdbx_chem_comp_identifier_item import PdbxChemCompIdentifierItem
from examples.schemas.pdbx_family_prd_audit_item import PdbxFamilyPrdAuditItem
from examples.schemas.pdbx_prd_audit_item import PdbxPrdAuditItem
from examples.schemas.pdbx_reference_entity_list_item import PdbxReferenceEntityListItem
from examples.schemas.pdbx_reference_entity_poly_item import PdbxReferenceEntityPolyItem
from examples.schemas.pdbx_reference_entity_poly_link_item import PdbxReferenceEntityPolyLinkItem
from examples.schemas.pdbx_reference_entity_poly_seq_item import PdbxReferenceEntityPolySeqItem
from examples.schemas.pdbx_reference_entity_sequence_item import PdbxReferenceEntitySequenceItem
from examples.schemas.pdbx_reference_entity_src_nat_item import PdbxReferenceEntitySrcNatItem
from examples.schemas.pdbx_reference_molecule import PdbxReferenceMolecule
from examples.schemas.pdbx_reference_molecule_annotation_item import PdbxReferenceMoleculeAnnotationItem
from examples.schemas.pdbx_reference_molecule_details_item import PdbxReferenceMoleculeDetailsItem
from examples.schemas.pdbx_reference_molecule_family import PdbxReferenceMoleculeFamily
from examples.schemas.pdbx_reference_molecule_features_item import PdbxReferenceMoleculeFeaturesItem
from examples.schemas.pdbx_reference_molecule_list_item import PdbxReferenceMoleculeListItem
from examples.schemas.pdbx_reference_molecule_related_structures_item import PdbxReferenceMoleculeRelatedStructuresItem
from examples.schemas.pdbx_reference_molecule_synonyms_item import PdbxReferenceMoleculeSynonymsItem
from examples.schemas.rcsb_bird_citation_item import RcsbBirdCitationItem
from examples.schemas.rcsb_chem_comp_annotation_item import RcsbChemCompAnnotationItem
from examples.schemas.rcsb_chem_comp_container_identifiers import RcsbChemCompContainerIdentifiers
from examples.schemas.rcsb_chem_comp_descriptor import RcsbChemCompDescriptor
from examples.schemas.rcsb_chem_comp_info import RcsbChemCompInfo
from examples.schemas.rcsb_chem_comp_related_item import RcsbChemCompRelatedItem
from examples.schemas.rcsb_chem_comp_synonyms_item import RcsbChemCompSynonymsItem
from examples.schemas.rcsb_chem_comp_target_item import RcsbChemCompTargetItem
from examples.schemas.rcsb_schema_container_identifiers_item import RcsbSchemaContainerIdentifiersItem


class ChemCompSchema(BaseModel):
	"""
	RCSB Exchange Database JSON schema derived from the bird_chem_comp_core content type schema. This schema supports collection bird_chem_comp_core version 7.1.3. This schema is hosted in repository https://github.com/rcsb/py-rcsb.db/tree/master/rcsb.db/data/json-schema/json-schema-min-bird_chem_comp_core.json and follows JSON schema specification version 4
	"""
	chem_comp: ChemComp | None = None
	pdbx_chem_comp_audit: List[PdbxChemCompAuditItem] | None = None
	pdbx_chem_comp_descriptor: List[PdbxChemCompDescriptorItem] | None = None
	pdbx_chem_comp_feature: List[PdbxChemCompFeatureItem] | None = None
	pdbx_chem_comp_identifier: List[PdbxChemCompIdentifierItem] | None = None
	pdbx_family_prd_audit: List[PdbxFamilyPrdAuditItem] | None = None
	pdbx_prd_audit: List[PdbxPrdAuditItem] | None = None
	pdbx_reference_entity_list: List[PdbxReferenceEntityListItem] | None = None
	pdbx_reference_entity_poly: List[PdbxReferenceEntityPolyItem] | None = None
	pdbx_reference_entity_poly_link: List[PdbxReferenceEntityPolyLinkItem] | None = None
	pdbx_reference_entity_poly_seq: List[PdbxReferenceEntityPolySeqItem] | None = None
	pdbx_reference_entity_sequence: List[PdbxReferenceEntitySequenceItem] | None = None
	pdbx_reference_entity_src_nat: List[PdbxReferenceEntitySrcNatItem] | None = None
	pdbx_reference_molecule: PdbxReferenceMolecule | None = None
	pdbx_reference_molecule_annotation: List[PdbxReferenceMoleculeAnnotationItem] | None = None
	pdbx_reference_molecule_details: List[PdbxReferenceMoleculeDetailsItem] | None = None
	pdbx_reference_molecule_family: PdbxReferenceMoleculeFamily | None = None
	pdbx_reference_molecule_features: List[PdbxReferenceMoleculeFeaturesItem] | None = None
	pdbx_reference_molecule_list: List[PdbxReferenceMoleculeListItem] | None = None
	pdbx_reference_molecule_related_structures: List[PdbxReferenceMoleculeRelatedStructuresItem] | None = None
	pdbx_reference_molecule_synonyms: List[PdbxReferenceMoleculeSynonymsItem] | None = None
	rcsb_bird_citation: List[RcsbBirdCitationItem] | None = None
	rcsb_chem_comp_annotation: List[RcsbChemCompAnnotationItem] | None = None
	rcsb_chem_comp_container_identifiers: RcsbChemCompContainerIdentifiers | None = None
	rcsb_chem_comp_descriptor: RcsbChemCompDescriptor | None = None
	rcsb_chem_comp_info: RcsbChemCompInfo | None = None
	rcsb_chem_comp_related: List[RcsbChemCompRelatedItem] | None = None
	rcsb_chem_comp_synonyms: List[RcsbChemCompSynonymsItem] | None = None
	rcsb_chem_comp_target: List[RcsbChemCompTargetItem] | None = None
	rcsb_schema_container_identifiers: List[RcsbSchemaContainerIdentifiersItem] | None = None
	rcsb_id: str
