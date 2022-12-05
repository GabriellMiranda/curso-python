# curso-python
# Lógica de Programação com python

# Teste em python

'''
O teste é formado por 3 etapas(GWT)

- Given - Dado
- When - Quando
- Then - Então
'''
bom que todos os tests sejam baseados em one_step

pytest -x test_qualquer_coisa => para o test no primeiro erro de test

pytest --pdb test_qualque_coisa => para exatamente na linha do erro e consigo verificar as variáveis

salvar os dados dos casos de testes:
pytest --junitxml report_1.xml

pytest -k 'goiabada' => vai rodar apenas os testes que tem goiabada no nome.
pytest -k cheese > vai rodar apenas os testes que tem o cheese.

pytest -s => vai mostrar os prints mostrando se o teste entrou em determinada parte do fluxo do código

salvar os dados dos casos de testes:
pytest --junitxml report_1.xml

Se você usar o marcador do pytest você consegue executar somente teste com aquele marcador:
Bom para criar um grupo de testes.
from pytest import mark

@mark.goiabada
def test_five_kidding_receive_five_so_return_five_goiabada():
    assert kidding(5) == 'goiabada'

    execução:
    pytest -m goiabada

    só irá executar os testes que tem marcador goiabada


@mark.skip => Para pular testes

@mark.skip(reason="Não foi implementado")
def test_fiften_kidding_receive_ten_so_return_fiften_goiabada():
    assert kidding(15) == 'goiabada'