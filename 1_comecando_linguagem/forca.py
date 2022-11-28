import random 

#printa mensagem de abertura
def print_message_opening():
    print(40*"*")
    print("Welcome to hangman game")
    print(40*"*")

#carrega palavra vazia
def carries_word_secret():
    file = open("entrada.txt","r")
    word = []
    for line in file:
        line = line.strip() # removendo \n e espaços das strings
        word.append(line)
    
    word_index = random.randrange(0, len(word))
    word_secret = word[word_index]
    file.close()
   
    return word_secret.upper()


def init_letter_hit(word_secret):
    return ["_" for letter in word_secret] 
 
def ask_kick_letter():
    kick = input("which letter?")
    kick = kick.strip() # tira todos os espaços da string 
    return kick.upper()

def brand_kick_right(kick, right_letters, word_secret, ):
    index = 0
    for letter in word_secret:
        if(letter == kick): #upper deixa todas as letra maiusculas
            right_letters[index] = letter
        index+=1

def draw_hanged(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def print_message_loser(word_secret):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(word_secret))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_messange_winner():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")



def game_hanged():

    print_message_opening()
    word_secret = carries_word_secret()
    right_letters = init_letter_hit(word_secret)    
    print(right_letters)

    hanged = hit = False
    mistakes = 0

    while(not hanged and not hit):
    
        kick = ask_kick_letter()
        print(kick)
        if(kick in word_secret):
            brand_kick_right(kick, right_letters, word_secret)
        else:
            mistakes+=1
            draw_hanged(mistakes)

        hit = "_" not in right_letters
        hanged = mistakes == 7
        print(right_letters)
    
    if(not hanged):
        print("Congragulations, you got the word right")
        print_messange_winner()
    else:
        print("Ops, you hanged yourself!")
        print_message_loser(word_secret)
    print("end game")

if(__name__ == "__main__"):
    game_hanged()