class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._like = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def like(self):
        return self._like

    def add_like(self):
        self._like+=1


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    
class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    

vingadores = Movie('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.add_like()
vingadores.add_like()
vingadores.add_like()

atlanta.add_like()
atlanta.add_like()

print(f'Nome: {vingadores.name} - Likes: {vingadores.like}')
print(f'Nome: {atlanta.name} - Likes: {atlanta.like}')