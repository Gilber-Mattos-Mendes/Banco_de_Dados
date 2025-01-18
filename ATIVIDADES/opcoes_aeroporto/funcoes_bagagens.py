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




def adicionar_bagagens():

    conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")
    cursor = conn.cursor()

    numero_bagagem = int(input(F'{CIAN}\t\t\tDigite o número da Bagagem: {RESET}'))
    destino = input(F'{CIAN}\t\t\tDestino: {RESET}')
    peso = float(input(F'{CIAN}\t\t\tPeso da Bagagem: {RESET}'))
    

    cursor.execute('''
    INSERT INTO bagagens (numero_bagagem, destino, peso)
    VALUES (?, ?, ?)
    ''', (numero_bagagem, destino, peso))

    conn.commit()
    conn.close()







def exibir_bagagens():

    conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bagagens")
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
    

