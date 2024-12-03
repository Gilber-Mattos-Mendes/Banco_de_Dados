import sqlite3
import os
from opcoes_aeroporto.funcoes_clientes import cadastro_cliente, passagens



conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")

cursor = conn.cursor()

def menu():
    while True:

        conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")

        cursor = conn.cursor()

        os.system('cls')
        
        print('-' *70)
        print("COMPANHIA AÉREA: ")
        print('-' *70)

        print('1- Atualizar Dados: \n'
              '2- Exibir Dados: \n'
              '3- Alterar Dados: '
              '4- Excluir Dados: ')
        print()

        escolha = int(input('Digite o número da opção escolhida: '))

        if escolha == 1:

            print('Atualizar')
            print('1- Cliente: '
                  '2- Passagem: ')

            atualizar = input('Digite o número da opção escolhida: ')

            if atualizar == 1:
                
                cadastro_cliente()
                print('Cliente Cadastrado!')
                
            elif atualizar == 2:

                passagens()
                print('Passagem atualizada!')         


menu()


conn.commit()
conn.close()