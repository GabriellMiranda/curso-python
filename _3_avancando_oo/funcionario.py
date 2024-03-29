class Funcionario:
    def registra_horas(self, horas: int) -> None:
        print('Horas registradas.')

    def mostrar_tarefas(self) -> None:
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self) -> None:
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None) -> None:
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self) -> None:
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self) -> None:
        print('Mostrando perguntas não respondidas do fórum')

class Alura(Funcionario):
     def mostrar_tarefas(self) -> None:
         print('Fez muita coisa, Alurete!')

class Hipster:
    def __str__(self) -> str:
        return f'Hipster,  {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Funcionario:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def registra_horas(self, horas: int) -> None:
        print('Horas registradas.')

    def mostrar_tarefas(self) -> None:
        print('Fez muita coisa...')


class Pleno(Alura, Caelum, Hipster):
    pass

# restante do código ...


jose = Junior('José')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

print(luan)