from typing import Dict, List, Union

from fila_base import FilaBase
from constants import CODIGO_PRIORITARIO
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

Classes = Union[EstatisticaDetalhada, EstatisticaResumida]

class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f"${CODIGO_PRIORITARIO}{self.codigo}"
    
    def chama_cliente(self, caixa:int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual} dirija-se ao caixa:{caixa}'

    def estatistica(self, retorna_estatistica: Classes) -> dict:
        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
        

if __name__=='__main__':
    fila_teste2 = FilaPrioritaria()
    fila_teste2.atualiza_fila()
    fila_teste2.atualiza_fila()
    fila_teste2.atualiza_fila()
    print(fila_teste2.chama_cliente(1))
    print(fila_teste2.estatistica(1,1,'detail'))