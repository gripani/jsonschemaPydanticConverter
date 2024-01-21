from pytest import fixture


@fixture
def idx() -> str:
    return "CFF"


@fixture
def api_endpoint() -> str:
    return "https://data.rcsb.org/rest/v1/core/chemcomp"


@fixture
def smile() -> str:
    return "O=C2N(c1ncn(c1C(=O)N2C)C)C"

