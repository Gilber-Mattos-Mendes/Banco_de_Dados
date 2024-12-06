import sqlite3
import os
from opcoes_aeroporto.funcoes_clientes import cadastro_cliente, atualizar_cadastro, exibir_clientes, excluir_cadastro
from opcoes_aeroporto.funcoes_passagens import adicionar_passagens



conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")

cursor = conn.cursor()


while True:

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")

    cursor = conn.cursor()

    
    print('-' *70)
    print("COMPANHIA AÉREA: ")
    print('-' *70)

    print('1- Acessar Área Cliente\n'
          '2- Acessar Área Passagens')
    print()

    escolha = int(input('Digite o número da opção escolhida: '))

    if escolha == 1:

        os.system('cls')

        print('1- Cadastrar Cliente\n'
              '2- Atualizar Dados\n'
              '3- Exibir Dados\n'
              '4- Excluir Dados')
        print()

        escolha_cliente = int(input('Digite o número da opção escolhida: '))

        if escolha_cliente == 1:
            
            cadastro_cliente()
            print('Cliente Cadastrado!')

            
        elif escolha_cliente == 2:

            atualizar_cadastro()
                   

        elif escolha_cliente == 3:

            exibir_clientes()

        elif escolha_cliente == 4:

            excluir_cadastro()

    elif escolha == 2:

        os.system('cls')

        print('1- Adicionar Passagem\n'
              '2- Atualizar Informações\n'
              '3- Exibir Passagens Cadastradas\n'
              '4- Excluir Passagem')
        print()

        escolha_passagem = int(input('Digite o número da opção escolhida: '))

        if escolha_passagem == 1:
            
            adicionar_passagens()

            
        elif escolha_passagem == 2:

            pass
                   

        elif escolha_passagem == 3:

            pass

        elif escolha_passagem == 4:

            pass




    conn.commit()
    conn.close()