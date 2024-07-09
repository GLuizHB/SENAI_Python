import os


nome = input('Nome: ')
idade = input('Sua idade: ')
idade = int(idade)
os.system('cls')

while True:
    print('Sala [1] - Deadpool e Wolverine - 18')
    print('Sala [2] - Meu malvado favorito 4 - L')
    print('Sala [3] - Divertida Mente 2 - L')
    print('Sala [4] - Maxxxine - 18')
    print('Sala [5] - Lugar Silencioso - 14')

    sala = input('Informe a Sala e Filme desejado: ')

    os.system('cls')
    
    if sala == '1':
        idade_minima = 16
    elif sala == '2':
        idade_minima = 14
    elif sala == '3':
        idade_minima = 12
    elif sala == '4':
        idade_minima = 0
    elif sala == '5':
        idade_minima = 18
    else:
        print('Sala inexistente. Favor escolher outra sala.')
        continue 

    if idade >= int(idade_minima):
        print(f'{nome} teve a entrada autorizada. Bom filme!')
        break
    else:
        print(f'{nome} não possui a idade mínima para o filme. Favor escolher outro filme.')
        continue

