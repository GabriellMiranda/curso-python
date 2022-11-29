
class Account:
    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__balance >= value:
            self.__balance -= value
        else:
            print("balance insufficient!!")

    def extract(self):
        print("Your balance is:{}, the holder: {}".format(self.__balance, self.__holder))

    def transfer(self, value, destiny): # tranfer money for other account
        self.withdraw(value)
        destiny.deposit(value)

    def get_balance(self):
        return self.__balance
    
    def get_holder(self):
        return self.__holder
    
    def get_limit(self):
        return self.__limit

    def set_limit(self, new_value):
        self.__limit = new_value

