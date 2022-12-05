from pytest import mark
from codeForTest.game import kidding

'''
O teste é formado por 3 etapas(GWT)

- Given - Dado
- When - Quando
- Then - Então
'''
#bom que todos os tests sejam baseados em one_step

# pytest -x test_qualquer_coisa - para o test no primeiro erro de test

# pytest --pdb test_qualque_coisa - para exatamente na linha do erro e consigo verificar as variáveis

# salvar os dados dos casos de testes:
# pytest --junitxml report_1.xml

#pytest -k goiabada - vai rodar apenas os testes que tem goiabada no nome.
#pytest -k cheese - vai rodar apenas os testes que tem o cheese.

#pytest -s = vai mostrar os prints mostrando se o teste entrou em determinada parte do fluxo do código


def test_when_Kidding_receive_one_so_return_one():
    entry = 1 # dado
    expected = 1 # dado
    result = kidding(entry) #quando - executando a função
    assert result == expected #então - validação da função 


def test_two_kidding_receive_two_so_return_two():
    #one step
    assert kidding(2) == 2

def test_tree_kidding_receive_tree_so_return_tree_cheese():
    assert kidding(3) == 'cheese'

@mark.goiabada
def test_five_kidding_receive_five_so_return_five_goiabada():
    assert kidding(5) == 'goiabada'

@mark.goiabada
def test_ten_kidding_receive_ten_so_return_ten_goiabada():
    assert kidding(10) == 'goiabada'

@mark.skip(reason="Não foi implementado")
def test_fiften_kidding_receive_ten_so_return_fiften_goiabada():
    assert kidding(15) == 'goiabada'