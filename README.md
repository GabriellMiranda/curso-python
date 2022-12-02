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

oi