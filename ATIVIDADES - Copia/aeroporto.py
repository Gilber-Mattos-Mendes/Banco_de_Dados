#===================================================================== IMPORTANDO BIBLIOTECAS E MÓDULOS ========================================================================
import sqlite3
import os
from opcoes_aeroporto.funcoes_clientes import cadastro_cliente, atualizar_cadastro, exibir_clientes, excluir_cadastro
from opcoes_aeroporto.funcoes_passagens import adicionar_passagens, excluir_passagem, atualizar_passagem, exibir_passagens



#========================================================================= MUDANDO VISUAL ====================================================================================
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CIAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"


#===================================================================== INICIALIZANDO O BANCO ==================================================================================

conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
cursor = conn.cursor()

#======================================================================== MENU ===============================================================================================

while True:

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")

    cursor = conn.cursor()

    
    print(F'{BOLD}{GREEN}-{RESET}' *70)
    print(f"{BOLD}{GREEN}\t\t\tCOMPANHIA AÉREA: {RESET}")
    print(F'{BOLD}{GREEN}-{RESET}' *70)

    print(F'{BOLD}{CIAN}\t\t\t1- Acessar Área Cliente\n'
          '\t\t\t2- Acessar Área Passagens\n'
          '\t\t\t3- Sair ')
    print()
    print(F'{BOLD}{GREEN}-{RESET}' *70)

    escolha = int(input(f'{BOLD}{GREEN}\t\t\tDigite o número da opção escolhida: {RESET}'))


#==================================================================== SUB MENU CLIENTE ======================================================================================
    
    if escolha == 1:

        os.system('cls')

        print(F'{BOLD}{GREEN}-{RESET}' *70)
        print(F'{CIAN}\t\t\t1- Cadastrar Cliente\n'
              '\t\t\t2- Atualizar Dados\n'
              '\t\t\t3- Exibir Dados\n'
              '\t\t\t4- Excluir Dados\n'
              '\t\t\t5- Voltar {RESET}')
        print()
        print(F'{BOLD}{GREEN}-{RESET}' *70)

        escolha_cliente = int(input(f'{BOLD}{GREEN}\t\t\tDigite o número da opção escolhida: {RESET}'))

        if escolha_cliente == 1:
            
            cadastro_cliente()

            print(F'{BOLD}{GREEN}-{RESET}' *70)
            concluido = input(F'{BOLD}{CIAN}\t\t\tCadastro Realizado com sucesso! Digite (S)sair (R)retomar: {RESET}').lower()

            if concluido == 's':
                
                break

            else:
                continue

            
        elif escolha_cliente == 2:

            atualizar_cadastro()

            print(F'{BOLD}{GREEN}-{RESET}' *70)
            concluido = input(F'{BOLD}{CIAN}\t\t\tDados Atualizados com sucesso! Digite (S)sair (R)retomar: {RESET}').lower()

            if concluido == 's':
                
                break

            else:
                continue
                   

        elif escolha_cliente == 3:

            exibir_clientes()

            print(F'{BOLD}{GREEN}-{RESET}' *70)
            concluido = input(F'{BOLD}{CIAN}\t\t\tExcluído com sucesso! Digite (S)sair (R)retomar: {RESET}').lower()

            if concluido == 's':
                
                break

            else:
                continue

            

        elif escolha_cliente == 4:

            excluir_cadastro()

            print(F'{BOLD}{GREEN}-{RESET}' *70)
            concluido = input(F'{BOLD}{RED}\t\t\tExcluído com sucesso! Digite (S)sair (R)retomar: {RESET}').lower()
            print(F'{BOLD}{GREEN}-{RESET}' *70)

            if concluido == 's':
                
                break

            else:
                continue

        
        elif escolha_cliente == 5:

            continue

        else:
            invalido = input(F'{BOLD}{CIAN}\t\t\tOpção inválida!\n'
                  '\t\t\tDeseja retornar? (s/n): {RESET}')
            print(F'{BOLD}{GREEN}-{RESET}' *70)
            
            if invalido == 's':
                continue

            else:
                print(F'{BOLD}{GREEN}-{RESET}' *70)
                print(F'{BOLD}{CIAN}\t\t\tfinalizando... {RESET}')
                print(F'{BOLD}{GREEN}-{RESET}' *70)
                break


#======================================================================= SUB MENU PASSAGENS =================================================================================

    elif escolha == 2:

        os.system('cls')

        print(F'{BOLD}{GREEN}-{RESET}' *70)
        print(F'{CIAN}\t\t\t1- Adicionar Passagem\n'
              '\t\t\t2- Atualizar Informações\n'
              '\t\t\t3- Exibir Passagens Cadastradas\n'
              '\t\t\t4- Excluir Passagem\n'
              '\t\t\t5- Voltar {RESET}')
        print()
        print(F'{BOLD}{GREEN}-{RESET}' *70)

        escolha_passagem = int(input(f'{BOLD}{GREEN}\t\t\tDigite o número da opção escolhida: {RESET}'))

        if escolha_passagem == 1:
            
            adicionar_passagens()

            print(F'{BOLD}{GREEN}-{RESET}' *70)
            concluido = input(F'{BOLD}{CIAN}\t\t\tPassagem Adicionada com sucesso! Digite (S)sair (R)retomar: {RESET}').lower()

            if concluido == 's':
                
                break

            else:
                continue


            
        elif escolha_passagem == 2:

            atualizar_passagem()

            print(F'{BOLD}{GREEN}-{RESET}' *70)
            concluido = input(F'{BOLD}{CIAN}\t\t\tPassagem atualizada com sucesso! Digite (S)sair (R)retomar: {RESET}').lower()

            if concluido == 's':
                
                break

            else:
                continue


                   

        elif escolha_passagem == 3:

            exibir_passagens()

            print(F'{BOLD}{GREEN}-{RESET}' *70)
            concluido = input(F'{BOLD}{CIAN}\t\t\tExcluído com sucesso! Digite (S)sair (R)retomar: {RESET}').lower()

            if concluido == 's':
                
                break

            else:
                continue
           

        elif escolha_passagem == 4:

            excluir_passagem()

            print(F'{BOLD}{GREEN}-{RESET}' *70)
            concluido = input(F'{BOLD}{CIAN}\t\t\tExcluído com sucesso! Digite (S)sair (R)retomar: {RESET}').lower()

            if concluido == 's':
                
                break

            else:
                continue

        
        elif escolha_passagem == 5:

            continue


        else:
            invalido = input(f'{BOLD}{GREEN}\t\t\tOpção inválida!\n'
                  '\t\t\tDeseja retornar? (s/n): {RESET}')
            print(F'{BOLD}{GREEN}-{RESET}' *70)
            
            if invalido == 's':
                continue

            else:
                print(F'{BOLD}{GREEN}-{RESET}' *70)
                print(F'{BOLD}{CIAN}\t\t\tfinalizando... {RESET}')
                print(F'{BOLD}{GREEN}-{RESET}' *70)
                break

    if escolha == 3:
        print(F'{BOLD}{GREEN}={RESET}' *70)
        print(F'{BOLD}{CIAN}Até mais... {RESET}')
        print(F'{BOLD}{GREEN}={RESET}' *70)
        break


conn.commit()
conn.close()
