import os
import sqlite3
from prettytable import PrettyTable 



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



def cadastro_cliente():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()

    nome = input(F'{CIAN}\t\t\tDigite seu Nome: {RESET}')
    idade = int(input(F'{CIAN}\t\t\tDigite a sua idade: {RESET}'))

                

    cursor.execute('''
    INSERT INTO clientes_cadastrados (nome, idade)
    VALUES (?, ?)
    ''', (nome, idade))

    conn.commit()
    conn.close()

def atualizar_cadastro():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()
    
    
    id_cliente = int(input(F'{CIAN}\t\t\tDigite o ID do cliente que deseja Atualizar: {RESET}'))
    nome = input(F'{CIAN}\t\t\tDigite o novo nome: {RESET}')
    idade = input(F'{CIAN}\t\t\tDigite a nova idade: {RESET}')
    
    cursor.execute(""" UPDATE clientes_cadastrados
        SET nome = ?, idade = ?
        WHERE id_cliente = ?
    """, (nome, idade, id_cliente))
    

    print(F'{CIAN}\t\t\tCadastro atualizado com sucesso! {RESET}')

    
    conn.commit()
    conn.close()


def exibir_clientes():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes_cadastrados")
    resultados = cursor.fetchall()


    # Cria a tabela Prettytable e define os nomes das colunas
    tabela = PrettyTable()
    # Obtém os nomes das colunas a partir de cursor.description
    colunas = [descricao[0] for descricao in cursor.description]
    # Define os nomes das colunas na tabela PrettyTable
    tabela.field_names = colunas

    # Adiciona as linhas à tabela
    for row in resultados:
        tabela.add_row(row)

    print(tabela)
    conn.close()


def excluir_cadastro():

    
    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()

    os.system('cls')

    id_cliente = input(F'{CIAN}\t\t\tDigite o ID do cliente para excluir: {RESET}')

    # Executa a exclusão com base no nome fornecido pelo usuário
    cursor.execute('DELETE FROM clientes_cadastrados WHERE id_cliente = ?', (id_cliente,))
    conn.commit()


    # Fecha a conexão
    conn.close()