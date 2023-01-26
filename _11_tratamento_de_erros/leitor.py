class LeitorDeArquivo:
    def __init__(self, arquivo) -> None:
        self.arquivo = arquivo
        print(f"Abrindo arquivo:{self.arquivo}")

    def ler_proxima_linha(self):
        print("Lendo linha...")
        return 'Linha de arquivo'
    
    def fechar(self):
        print("Fechando arquivo.")

try:
    leitor = LeitorDeArquivo("arquivo.txt")
    leitor.ler_proxima_linha()
    leitor.ler_proxima_linha()
    leitor.ler_proxima_linha()
except IOError as E:
    print(E)
finally:
    leitor.fechar()

