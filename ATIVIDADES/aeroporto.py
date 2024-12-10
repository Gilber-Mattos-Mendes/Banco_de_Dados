
import sqlite3
import os
from opcoes_aeroporto.funcoes_clientes import cadastro_cliente, atualizar_cadastro, exibir_clientes, excluir_cadastro
from opcoes_aeroporto.funcoes_passagens import adicionar_passagens, excluir_passagem, atualizar_passagem, exibir_passagens



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

            concluido = input('Cadastro Realizado com sucesso! Digite (S)sair (R)retomar:')

            if concluido == 's':
                
                break

            else:
                continue

            
        elif escolha_cliente == 2:

            atualizar_cadastro()
            concluido = input('Dados Atualizados com sucesso! Digite (S)sair (R)retomar:')

            if concluido == 's':
                
                break

            else:
                continue
                   

        elif escolha_cliente == 3:

            exibir_clientes()

            concluido = input('Excluído com sucesso! Digite (S)sair (R)retomar:')

            if concluido == 's':
                
                break

            else:
                continue

            

        elif escolha_cliente == 4:

            excluir_cadastro()

            concluido = input('Excluído com sucesso! Digite (S)sair (R)retomar:')

            if concluido == 's':
                
                break

            else:
                continue


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
<<<<<<< HEAD
            
            concluido = input('Passagem Adicionada com sucesso! Digite (S)sair (R)retomar:')

            if concluido == 's':
                
                break

            else:
                continue
=======
            print('Passagem cadastrada com sucesso!')
>>>>>>> 1a5217f6b3f0e81f4f06ef33e310390bb06ba5c6

            
        elif escolha_passagem == 2:

            atualizar_passagem()
<<<<<<< HEAD

            concluido = input('Passagem atualizada com sucesso! Digite (S)sair (R)retomar:')

            if concluido == 's':
                
                break

            else:
                continue
=======
>>>>>>> 1a5217f6b3f0e81f4f06ef33e310390bb06ba5c6
                   

        elif escolha_passagem == 3:

            exibir_passagens()
<<<<<<< HEAD

            concluido = input('Excluído com sucesso! Digite (S)sair (R)retomar:')

            if concluido == 's':
                
                break

            else:
                continue
           

=======
>>>>>>> 1a5217f6b3f0e81f4f06ef33e310390bb06ba5c6

        elif escolha_passagem == 4:

            excluir_passagem()

            concluido = input('Excluído com sucesso! Digite (S)sair (R)retomar:')

            if concluido == 's':
                
                break

            else:
                continue


    conn.commit()
    conn.close()
