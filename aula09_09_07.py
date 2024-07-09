import random

'''
nome1 = input('Digite um nome: ')
nome2 = input('Digite um nome: ')
nome3 = input('Digite um nome: ')
nome4 = input('Digite um nome: ')
nome5 = input('Digite um nome: ')

lista_nome = [nome1, nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_nome)

print(f'O sorteado foi {escolhido}')

'''
'''
lista_nome = []

while True
    nome = input('Digite os nomes que serão sorteados: ')
    if nome != '':
        lista_nome.append(nome)
    else:
        break

escolhido = random.choice(lista_nome)

print(f'O sorteado foi {escolhido}')
print(lista_nome)
'''

import random
import os

lista_nome = []
lista_sorteados = []

while True:
    nome = input('Digite os nomes que serão sorteados: ')
    if nome != '':
        lista_nome.append(nome)
    else:
        break

while True:
    if lista_nome:
        os.system('cls')
        escolhido = random.choice(lista_nome)
        lista_sorteados.append(escolhido)
        print(f'O sorteado é {escolhido}')

        opcao = input('Deseja sortear outro nome? (s/n)').lower()
        os.system('cls')

        if opcao != 's':
            break

    else:
        print('Não existe números para seram sorteados')

print('Programa Finalizado')
print(f'Lista dos nomes: {lista_nome}')
print(f'Lista de Sorteados: {lista_sorteados}')