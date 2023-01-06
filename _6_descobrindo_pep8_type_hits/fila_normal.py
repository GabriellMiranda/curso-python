from fila_base import FilaBase

class FilaNormal(FilaBase):

    def atualizafila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senhaatual)
    
    def chamacliente(self, caixa:int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual} dirija-se ao caixa:{caixa}')


if __name__=="__main__":
    fila_teste = FilaNormal()
    fila_teste.atualizafila()
    fila_teste.atualizafila()
    fila_teste.atualizafila()
    fila_teste.atualizafila()
    fila_teste.atualizafila()
    print(fila_teste.chamacliente(1))
    print(fila_teste.chamacliente(1))
    