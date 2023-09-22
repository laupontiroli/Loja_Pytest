import pytest 
from ..db.db_utils import cadastro

@pytest.mark.cadastro 
def cadastro_idade_invalida():
    assert cadastro(200)== False