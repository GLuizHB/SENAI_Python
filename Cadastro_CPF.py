import time

lista_cpf = ['111.222.333-44','222.333.444.55','333.444.555-66','444.555.666-77']
lista_nome = ['gomes','oliveira']

while True:
    print(30*'-', 'BEM VINDO AO PYTHON CADASTRO', 30*'-')
    print('1. Cadastrar um novo usuário')
    print('2. Acessar o Sitema')
    print('3. Listar usuário')
    print('4. Excluir usuário')
    print('5. Sair')
    opcao = input('Digite a opção: ')
    opcao = int(opcao)

# Opção cadastrar um cpf
    if opcao == 1:
        novo_nome = input('Digite um novo nome que deseja cadastrar: ')
        novo_cpf = input('Digite um novo cpf: ')

        if novo_cpf in lista_cpf:
            print('CPF já cadastrado')
        else:
            lista_cpf.append(novo_cpf)
            lista_nome.append(novo_nome)
            print('CPF cadastrado com sucesso')

# Opção para acessar o sistema
    elif opcao == 2:
        cpf = input('Digite o cpf: ')

        if cpf in lista_cpf:
            print('Usuario logado com sucesso')

        for i in lista_nome:
            print(f'Usuário: {i}')

# Opção para listar os usuários na lista
    elif opcao == 3:
        print('Lista de Usuários')

        for i in lista_nome:
            time.sleep(2)
            print(f'Usuário: {i}')

# Opção para exclurir um cpf
    elif opcao == 4:
        excluir_cpf = input('Digite o CPF que deseja excluir: ')

        if excluir_cpf in lista_cpf:
            lista_cpf.remote(excluir_cpf)
            print('CPF excluido com sucesso!')
            time.sleep(3)

        else:
            print('Saindo do sistema')

# Opção para sair do sistema
    elif opcao == 5:
        print('Saindo do sistema!')
        time.sleep(3)
        break


    else:
        print('Opção invalida!')


print('Você esta fora do sistema!')
