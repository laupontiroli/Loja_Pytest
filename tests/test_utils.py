import pytest 
from ..db.db_utils import cadastro

@pytest.mark.cadastro 
def test_cadastro_idade_invalida():
    assert cadastro()== False

