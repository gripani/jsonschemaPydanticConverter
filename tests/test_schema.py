from httpx import get

from examples.schemas.chem_comp_schema import ChemCompSchema


def test_smiles(idx: str, api_endpoint: str, smile: str):

    response = get(f"{api_endpoint}/{idx}")

    json_response = response.json()
    chem_comp_schema = ChemCompSchema.model_validate(json_response)

    if chem_comp_schema.pdbx_chem_comp_descriptor is not None:
        pdbx_chem_comp_descriptor = chem_comp_schema.pdbx_chem_comp_descriptor[0]
        descriptor = pdbx_chem_comp_descriptor.descriptor
        if descriptor is not None:
            assert descriptor == smile
