import random

def difficulty ():
    #Escolhe a dificuldade do jogo de acordo com o digitado
    difficulty = input('Escolha a dificuldade do jogo: Fácil, "Intermediário ou Difícil" ')
    if difficulty == "Fácil":
        print('Vou pensar em um número de 1 a 20, e você tem que adivinhar')
        return 20
    elif difficulty == "Intermediario":
            print('Vou pensar em um número de 1 a 100, e você tem que adivinhar')
            return 100
    else:
        print('Vou pensar em um número de 1 a 300, e você tem que adivinhar')
        return 300
    
def the_game(secret_number):
    #Executando o jogo
    attempts = 0
    while True:
        attempts += 1
        round = int (input('Digite um número: '))

        if round == secret_number:
            print(f'"Parabéns, você acertou o número em {attempts} tentativas." ')
            break
        elif round < secret_number:
            print ('O número que você digitou é menor que o numero secreto')
        else:
            print('O número que você digitou é maior que o número secreto') 
#Obtem a dificuldade digitada
difficulty_level = difficulty()
#Gera o numero secreto
secret_number = random.randint (1, difficulty_level)
#Inicia o jogo
the_game(secret_number)

