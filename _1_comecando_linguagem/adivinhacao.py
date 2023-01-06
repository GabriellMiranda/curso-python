import random as rd

def joga_adivinhacao():
    print(40*"*")
    print("Bem vindo ao jogo de adivinhação")
    print(40*"*")

    numero_secreto = rd.randrange(1, 100)
    print("{}".format(numero_secreto))
    total_tentativas = 0
    total_pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) nível fácil (2) nível médio (3) nível difícil")

    nivel = int(input("Defina o nivel:"))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    while(total_tentativas > 0):
        print("Numero de tentativas:{}".format(total_tentativas))

        chute = int(input("Digite seu número:"))
        acertou =  (chute == numero_secreto)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue # esse continue não vai sair do laço, ele vai para outra iteração do while, parando o fluxo
                    # de execução aqui e criando outro. continue com a proxima rodada.
        if (acertou):
            print("Você acertou e fez {} pontos!".format(total_pontos))
            break
        else:
            if (chute < numero_secreto):
                total_pontos -= chute
                print("O chute foi menor que o número secreto!")
            elif (chute > numero_secreto):
                total_pontos -= chute
                print("O chute foi maior que o número secreto!")
            print("Você errou")
        total_tentativas-=1
        if (total_tentativas == 0):
            print("Você encerrou o total de tentativas!")

if(__name__ == "__main__"):
    joga_adivinhacao()