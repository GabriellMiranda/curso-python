class Contato:

    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

try:
    arquivo_contato = open('dados/contatos.csv')
except FileExistsError as e:
    print(e)
conteudo = arquivo_contato.readline()

print(conteudo)