from module.function import *

def menu():
    print('')
    print('<========== Bem vindo ao seu gerenciador de paciente e psicologo ==========>')
    print('1- Paciente')
    print('2- Psicologo')
    print('3- Saida do sistema')

    op = int(input('Digite a opção: '))

    if op == 1:
        menu_paciente()
    elif op == 2:
        menu_psicologo()
    elif op == 3:
        print('Fechando o sistema...')
        exit()
    else:
        print('Opção invalida!')
        return  menu()

def menu_paciente():
    print('<========== Gerenciador de paciente ==========>')
    print(' ')
    print('1- Novo paciente')
    print('2- listas pacientes')
    print('3- Atualizar cadastro paciente')
    print('4- Deletar cadastro paciente')
    print('5- Retornar ao menu principal')
    print(' ')
    op = int(input('Digite a opção: '))

    if op == 1:
        print('======> Novo paciente')
        print('====> Dados nescessarios:')
        print(' ')
        primeiro_nome = input('Digite o primeiro nome: ')
        ultimo_nome = input('Digite o sobre-nome: ')
        email = input('Digite o email: ')
        senha = input('Digite uma senha: ')
        create_paciente(primeiro_nome,ultimo_nome,email,senha)
        return menu_paciente()
    elif op == 2:
        tabela = 'paciente'
        listagem(tabela)
        return menu_paciente()
    elif op == 3:
        print('======> Atualização de cadastro paciente')
        print('====> Dados nescessarios:')
        print(' ')
        tabela = 'paciente'
        id = input('Identificados do paciente: ')
        primeiro_nome = input('Primiro nome: ')
        ultimo_nome = input('Último nome: ')
        email = input('Email de acesso: ')
        senha = input('Senha de acesso:')
        atualizacao(tabela,id,primeiro_nome,ultimo_nome,email,senha)
        return menu_paciente()
    elif op == 4:
        print('======> Exclução de paciente')
        print('====> Dados nescessarios:')
        print(' ')
        tabela = 'paciente'
        id = int(input('Identificados do paciente: '))
        exclucao(tabela,id)
        return menu_paciente()
    elif op == 5:
        menu()
    else:
        print('Opção invalida!')
        return menu_paciente()

def menu_psicologo():
    print('<========== Gerenciador de psicologo ==========>')
    print('1- Novo psicologo')
    print('2- listas psicologos')
    print('3- Atualizar cadastro psicologo')
    print('4- Deletar cadastro psicologo')
    print('5- Retornar ao menu principal')

    op = int(input('Digite a opção: '))

    if op == 1:
        print('======> Novo psicologo')
        print('====> Dados nescessarios:')
        print(' ')
        primeiro_nome = input('Digite o primeiro nome: ')
        ultimo_nome = input('Digite o sobre-nome: ')
        email = input('Digite o email: ')
        senha = input('Digite uma senha: ')
        create_psicologo(primeiro_nome, ultimo_nome, email, senha)
        return menu_psicologo()
    elif op == 2:
        tabela = 'psicologo'
        listagem(tabela)
        return menu_psicologo()
    elif op == 3:
        print('======> Atualização de cadastro psicologo')
        print('====> Dados nescessarios:')
        print(' ')
        tabela = 'psicologo'
        id = input('Identificados do psicologo: ')
        primeiro_nome = input('Primiro nome: ')
        ultimo_nome = input('Último nome: ')
        email = input('Email de acesso: ')
        senha = input('Senha de acesso:')
        atualizacao(tabela, id, primeiro_nome, ultimo_nome, email, senha)
        return menu_psicologo()
    elif op == 4:
        print('======> Exclução de psicologo')
        print('====> Dados nescessarios:')
        print(' ')
        tabela = 'psicologo'
        id = int(input('Identificados do paciente: '))
        exclucao(tabela, id)
        return menu_psicologo()
    elif op == 5:
        menu()
    else:
        print('Opção invalida!')
        return menu_psicologo()


if __name__ == '__main__':
    menu()