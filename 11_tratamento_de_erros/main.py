from exceptions import SaldoInsuficienteError, OperacaoFinanceiraError

class Cliente:
    def __init__(self, nome: str, cpf: str, profissao: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente: Cliente, agencia: int, numero: int) -> None:
        self.__saldo = 100
        self.__agencia =0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidas = 0


        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30/ContaCorrente.total_contas_criadas

    @property
    def agencia(self) -> int:
        return self.__agencia

    def __set_agencia(self, value: float) -> None:
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser um inteiro", value)
        if value <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")
            
        self.__agencia = value


    @property
    def numero(self) -> int:
        return self.__numero

    def __set_numero(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("O atributo número deve ser um inteiro")
        if value <= 0:
            raise ValueError("O atributo número  deve ser maior que zero")
        self.__numero = value


    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, value: float) -> None:
        if not isinstance(value, float):
            raise ValueError("O atributo saldo deve ser um inteiro")

    def transferir(self, valor: float, favorecido: Cliente) -> None:
        if valor > 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidas += 1
            E.args = ()
            raise OperacaoFinanceiraError("Operação não finalizada") from E
        favorecido.depositar(valor)
    
    def sacar(self, valor: float) -> None:
        if valor > 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        if self.saldo < valor:
            self.saques_nao_permitidos += 1
            raise SaldoInsuficienteError(saldo=self.saldo, valor=valor)
        self.saldo -= valor

    def depositar(self, valor: float) -> None:
        self.saldo += valor

    def __str__(self) -> str:
        return f'saldo:{self.saldo}, agencia: {self.agencia}, numero: {self.numero}'


def main():
    import sys

    contas =[]
    while(True):
        try:
            nome = input("Nome do cliente: \n")
            agencia = input("Número da agência: \n")
            breakpoint()
            numero = input("Número da conta corrente: \n")

            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append = conta_corrente
        except KeyboardInterrupt:
            print(f"\n\n {len(contas)} conta(s) criadas")
            sys.exit()


conta_corrente1 = ContaCorrente(None, 400, 12345)
conta_corrente2 = ContaCorrente(None, 401, 12345)

conta_corrente1.transferir(110, conta_corrente2)
print('ContaCorrente1 Saldo: ', conta_corrente1.saldo)
print('ContaCorrente2 Saldo: ', conta_corrente2.saldo)

