
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age 
    
    @property # executa por baixo dos panos esse método ao invés de chamar o atributo name
    def name(self):
        return self.__name.title()