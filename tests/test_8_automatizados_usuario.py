import pytest
from _8_testes_altomatizados.src.leilao.dominio import Usuario, Leilao, LanceInvalido

@pytest.fixture
def usuario():
    return Usuario('Vine', 100.0)

@pytest.fixture
def leilao():
    return Leilao('celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(usuario, leilao):
    usuario.propoe_lance(leilao, 50.0)
    assert usuario.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(usuario, leilao):
    usuario.propoe_lance(leilao, 1.0)

    assert usuario.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_lance_e_igual_ao_valor_da_carteira(usuario, leilao):
    usuario.propoe_lance(leilao, 100.0)

    assert usuario.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(usuario, leilao):
    with pytest.raises(LanceInvalido):
        usuario.propoe_lance(leilao, 200.0)

