class SaldoInsuficienteError(Exception):
    def __init__(self, message='', saldo=None, valor=None, *args) -> None:
        self.saldo = saldo
        self.valor = valor
        msg = 'Saldo insuficiente para efetuar a transação ' \
            f'Saldo atual:{self.saldo} Valor a ser sacado: {self.valor}'
        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(self.msg, self.saldo, self.valor, *args)

class OperacaoFinanceiraError():
    pass