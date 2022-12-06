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

    def __str__(self):
        return (f'Name: {self.name} - year:{self.year} - Likes: {self._like}')

class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return (f'Name: {self.name} - Year:{self.year} - Duration:{self.duration} - Likes: {self._like}')

    
class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return (f'Name: {self.name} - Year:{self.year} - Seasons:{self.seasons} - Likes: {self._like}')

class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    @property
    def listing(self):
        return self._programs

    @property
    def listing(self):
        return self._programs

    @property
    def size(self):
        return len(self._programs)


vingadores = Movie('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Movie("Todo Mundo em Pânico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.add_like()
tmep.add_like()
vingadores.add_like()
demolidor.add_like()
vingadores.add_like()

atlanta.add_like()
atlanta.add_like()


movie_and_series = [vingadores, atlanta, demolidor, tmep]
playlist_end_in_week = Playlist('fim de semana', movie_and_series)
for program in playlist_end_in_week.listing:
    print(program)


print(f'Tá ou não tá? {demolidor in playlist_end_in_week.listing}')