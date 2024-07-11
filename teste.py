import os

os.system('cls')
while True:
    idade = input('Sua idade: ')
    idade = int(idade)

    print('Sala 1 - Deadpool e Wolverine - 18')
    print('Sala 2 - Meu malvado favorito 4 - L')
    print('Sala 3 - Divertida Mente 2 - L')
    print('Sala 4 - Maxxxine - 18')
    print('Sala 5 - Lugar Silencioso - 14')

    sala = input('Informe a Sala e Filme desejado: ')

    s01 = '1'
    s02 = '2'
    s03 = '3'
    s04 = '4'
    s05 = '5'


'''
    if idade >= 18:
        if sala == s01 or s04:
            print('\nEntrada permitida!')
        else:
            print('\nNão tem idade para assistir esse flime.')
    elif idade >= 14:
        if sala == s05:
            print('\nEntrada permitida!')
        else:
            print('\nNão tem idade para assistir esse filme.')
    else:
        print('\nClassificação livre.')
        continue
'''
    if sala == '1':
        if idade >= 18:
            print('Entrada pemitida.')
        