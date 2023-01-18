class LanceInvalido(Exception):
    pass

class Usuario:

    def __init__(self, nome: str, carteira: float) -> None:
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self.valor_eh_valido(valor):
            raise LanceInvalido("Seu saldo é insuficiente")

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    def valor_eh_valido(self, valor):
        return valor <= self.carteira
    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def carteira(self) -> str:
        return self.__carteira



class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self._lance_valido:
            if not self._tem_lances():
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise LanceInvalido('Erro ao propor lance')

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario
    
    def _valor_maior_que_o_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_valido(self, lance):
        return self._tem_lances() or self._usuarios_diferentes(lance) and self._valor_maior_que_o_anterior(lance)
    
    @property
    def lances(self):
        return self.__lances[:]
