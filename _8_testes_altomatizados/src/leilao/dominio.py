import sys

class Usuario:

    def __init__(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome


class Lance:

    def __init__(self, usuario: str, valor: float) -> None:
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao: str) -> None:
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self) -> str:
        return self.__lances

class Avaliador:

    def __init__(self) -> None:
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def avalia(self, leilao: Leilao) -> None:
        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor