import os
import time

cont = int(input('Digite um número inteiro: '))

while cont >= 0:
    os.system('cls') #Limpar o terminal
    print(f'Contagem regressiva: {cont} ...')
    time.sleep(1) # Atrasa o proximo comando 
    cont -= 1

os.system('cls')
print('BOOOOOOOOOOOOMMMMMMMMM!!!')
