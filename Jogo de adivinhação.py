
# Jogo de adivinhação

import random
numero_secreto = random.randint(1, 20)

# FIXME: Declarando variaveis

tentativas = 0
max_tentativas = 5
acertou = False

print('Bem vindo ao GAME Python Adivinha!!!')
print(f'Você tem {max_tentativas} tentativas para adivinhar o número secreto entre 1 e 20')

# loop (jogo)

while tentativas < max_tentativas:
    palpite = int(input('Digite um número inteiro entre 1 e 20: '))

    tentativas += 1

    if palpite == numero_secreto:
        acertou = True
        break

    elif palpite < numero_secreto:
        print('Tente um número maior')
    else:
        print('Tente um número menor')
if acertou:
    print(f'Parabens! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.')
else:
    print(f'Que pena! Você não  conseguiu adivinhar o número secreto {numero_secreto} ')