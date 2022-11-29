
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age 
    
    @property # executa por baixo dos panos esse método ao invés de chamar o atributo name
    def name(self):
        return self.__name.title()

    @name.setter # funciona para acessar direto
    def name(self, name):
        self.__name = name

person = Person("gabriel", 21)

print(person.name)

person.name = "Erike"
print(person.name)