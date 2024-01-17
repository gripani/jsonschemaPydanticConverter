from httpx import get

from examples.schemas.chem_comp_schema import ChemCompSchema


def test_smiles(idx: str = "CFF"):

    response = get(f"https://data.rcsb.org/rest/v1/core/chemcomp/{idx}")

    json_response = response.json()
    chem_comp_schema = ChemCompSchema.model_validate(json_response)

    if chem_comp_schema.pdbx_chem_comp_descriptor is not None:
        pdbx_chem_comp_descriptor = chem_comp_schema.pdbx_chem_comp_descriptor[0]
        descriptor = pdbx_chem_comp_descriptor.descriptor
        comp_id = pdbx_chem_comp_descriptor.comp_id
        if descriptor is not None:
            assert descriptor == "O=C2N(c1ncn(c1C(=O)N2C)C)C"
            assert comp_id == idx




