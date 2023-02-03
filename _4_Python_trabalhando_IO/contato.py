class Contato:

    def __init__(self, id: int, nome: str, email: str) -> None:
        self.id = id
        self.nome = nome
        self.email = email


if __name__=='__main__':
    try:
        arquivo_contato = open('dados/contatos.csv')
    except FileExistsError as e:
        print(e)
    conteudo = arquivo_contato.readline()

    print(conteudo)