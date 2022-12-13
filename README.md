# curso-python
# Lógica de Programação com python

# 1_comecando_linguagem
    Conceitos básicos de lógica de programação na linguagem python
    utilização de comandos como:
    if, for, while.

# 2_orientação_a_objetos
    Criação de classes em python.
    criação de métodos estáticos:

        @staticmethod
        def code_bank():
            return "001"

    Criação de métodos com o @property:

        @property # executa por baixo dos panos esse método ao invés de chamar o atributo name
        def name(self):
            return self.__name.title()

    Criação de métodos com o setter:

        @name.setter # funciona para acessar direto
        def name(self, name):
            self.__name = name

# 3_avançando_oo
    Entendendo mais sobre herança e polimorfimo

    Exemplo de herança em python:

        class Movie(Program):
        def __init__(self, name, year, duration):
            super().__init__(name, year)
            self.duration = duration

        Movie herda funcionalidade e atributos da classe mãe Program
    
    Usando o médoto __str__:

        def __str__(self):
        return (f'Name: {self.name} - Year:{self.year} - Duration:{self.duration} - Likes: {self._like}')

        Serve para printar a classe, sem precisar chamar algum método
    
    Usando o método __getitem__:

            #Transformando a playlist em uma lista sem herdar de list
    def __getitem__(self, item):
        return self._programs[item]

        Transforma um atributo da classe em um iterável, podem iterar sobre a classe.

    Herança múltipla:

        class Pleno(Alura, Caelum):
    pass




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

    