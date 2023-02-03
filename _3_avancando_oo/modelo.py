class Program:
    def __init__(self, name: str, year: int) -> None:
        self._name = name.title()
        self.year = year
        self._like = 0

    @property
    def name(self) -> None:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def like(self) -> int:
        return self._like

    def add_like(self) -> None:
        self._like+=1

    def __str__(self) -> str:
        return (f'Name: {self.name} - year:{self.year} - Likes: {self._like}')

class Movie(Program):
    def __init__(self, name: str, year: int, duration: int) -> None:
        super().__init__(name, year)
        self.duration = duration

    def __str__(self) -> str:
        return (f'Name: {self.name} - Year:{self.year} - Duration:{self.duration} - Likes: {self._like}')

    
class Serie(Program):
    def __init__(self, name: str, year: int, seasons: int) -> None:
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self) -> str:
        return (f'Name: {self.name} - Year:{self.year} - Seasons:{self.seasons} - Likes: {self._like}')

class Playlist:
    def __init__(self, name: str, programs) -> None:
        self.name = name
        self._programs = programs

    #Transformando a playlist em uma lista sem herdar de list
    def __getitem__(self, item: int):
        return self._programs[item]

    @property
    def listing(self) -> Program:
        return self._programs

    @property
    def listing(self) -> Program:
        return self._programs

    def __len__(self) -> int:
        return len(self._programs)


if __name__=='__main__':
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
    for program in playlist_end_in_week:
        print(program)


    print(f'Tá ou não tá? {demolidor in playlist_end_in_week.listing}')