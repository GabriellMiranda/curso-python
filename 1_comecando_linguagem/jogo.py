import forca
import adivinhacao

def escolhe_jogo():
    print(40*"*")
    print("Escolha seu jogo!")
    print(40*"*")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("jogando adivinhação")
        adivinhacao.joga_adivinhacao()

if (__name__ == "__main__"):
    escolhe_jogo()