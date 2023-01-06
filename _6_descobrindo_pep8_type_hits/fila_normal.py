from fila_base import FilaBase

from constants import CODIGO_NORMAL

class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f"${CODIGO_NORMAL}{self.codigo}"

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)
    
    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual} dirija-se ao caixa:{caixa}')


if __name__=="__main__":
    fila_teste = FilaNormal()
    fila_teste.atualiza_fila()
    fila_teste.atualiza_fila()
    fila_teste.atualiza_fila()
    fila_teste.atualiza_fila()
    fila_teste.atualiza_fila()
    print(fila_teste.chama_cliente(1))
    print(fila_teste.chama_cliente(1))
    