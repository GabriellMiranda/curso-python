
class Account:
    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        self.__code_bank = "001"

    def deposit(self, value):
        self.__balance += value

    def __can_withdraw(self, value): #método que poder ser usado somente dentro da classe
        return (self.__balance + self.__limit) >= value

    def withdraw(self, value):
        if (self.can_withdraw(value)):
            self.__balance -= value
        else:
            print("limit insufficient!!")

    def extract(self):
        print("Your balance is:{}, the holder: {}".format(self.__balance, self.__holder))

    def transfer(self, value, destiny): # tranfer money for other account
        self.withdraw(value)
        destiny.deposit(value)

    def get_balance(self):
        return self.__balance
    
    def get_holder(self):
        return self.__holder

    @property # é usado como um get e pode ser acessado diretamente como ser fosse variável, mas é função ex: account.limit 
    def limit(self):
        return self.__limit

    @limit.setter # usar como set ex: account.limit = 1000, mas tá usando a função não o atributo
    def limit(self, new_value):
        self.__limit = new_value

    @staticmethod
    def code_bank():
        return "001"

    @staticmethod # pode ser acessado sem criar um referencia de conta
    def code_banks():
        return {'BB':'001','Caixa':'104', 'Bradesco':'1'}

account = Account(1, "gabriel",50,1000)
account.extract()