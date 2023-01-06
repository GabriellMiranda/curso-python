from fila_base import FilaBase

class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f"NM{self.codigo}"
  
    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)
    
    def chama_cliente(self, caixa:int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual} dirija-se ao caixa:{caixa}'

    def estatistica(self, dia: int, agencia: int, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia}-{dia}':len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['cliente_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_clientes_atendidos'] = len(
                self.clientes_atendidos)

        return estatistica

if __name__=='__main__':
    fila_teste2 = FilaPrioritaria()
    fila_teste2.atualiza_fila()
    fila_teste2.atualiza_fila()
    fila_teste2.atualiza_fila()
    print(fila_teste2.chama_cliente(1))
    print(fila_teste2.estatistica(1,1,'detail'))