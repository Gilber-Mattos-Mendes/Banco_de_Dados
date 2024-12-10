import os
import sqlite3
from prettytable import PrettyTable 



def cadastro_cliente():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()

    nome = input('Digite seu Nome: ')
    idade = int(input('Digite a sua idade: '))

                

    cursor.execute('''
    INSERT INTO clientes_cadastrados (nome, idade)
    VALUES (?, ?)
    ''', (nome, idade))

    conn.commit()
    conn.close()

def atualizar_cadastro():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()
    
    
    id_cliente = int(input('Digite o ID do cliente que deseja Atualizar: '))
    nome = input('Digite o novo nome: ')
    idade = input('Digite a nova idade: ')
    
    cursor.execute("""
<<<<<<< HEAD
        UPDATE clientes_cadastrados 
=======
        UPDATE clientes 
>>>>>>> 1a5217f6b3f0e81f4f06ef33e310390bb06ba5c6
        SET nome = ?, idade = ?
        WHERE id_cliente = ?
    """, (nome, idade, id_cliente))
    
<<<<<<< HEAD
=======
    print('Cadastro atualizado com sucesso!')
>>>>>>> 1a5217f6b3f0e81f4f06ef33e310390bb06ba5c6
    
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

    nome_cliente = input('Digite o nome do cliente para excluir: ')

    # Executa a exclusão com base no nome fornecido pelo usuário
    cursor.execute('DELETE FROM clientes_cadastrados WHERE nome = ?', (nome_cliente,))
    conn.commit()


    # Fecha a conexão
    conn.close()