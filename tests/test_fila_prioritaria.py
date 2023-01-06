import pytest
from _6_descobrindo_pep8_type_hits.fila_prioritaria import FilaPrioritaria



def test_gera_senha_atual():
    fila_prioritaria = FilaPrioritaria()
    fila_prioritaria.atualiza_fila()

    fila_prioritaria.gera_senha_atual()
    print(fila_prioritaria.senha_atual)
    assert fila_prioritaria.senha_atual == 'NM1'

def test_reseta_fila_codigo_maio_100():
    fila_prioritaria = FilaPrioritaria()
