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



def adicionar_passagens():

    conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")
    cursor = conn.cursor()

    numero_voo = int(input(F'{CIAN}\t\t\tDigite o número do Voo: {RESET}'))
    id_cliente = int(input('Digite o ID do Cliente: '))
    id_bagagem = int(input('Digite i ID da Bagagem'))
    destino = input(F'{CIAN}\t\t\tDestino: {RESET}')
    preco_viagem = float(input(F'{CIAN}\t\t\tPreço da viagem: {RESET}'))
    data = input(F'{CIAN}\t\t\tData da viagem: {RESET}')

    cursor.execute('''
    INSERT INTO dados_viagem (numero_voo, id_cliente, id_bagagens, destino, preco_viagem, data)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (numero_voo, id_cliente, id_bagagem, destino, preco_viagem, data))

    conn.commit()
    conn.close()
    
    
    
    
def atualizar_viagem():
    
    conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")
    cursor = conn.cursor()
    
    
    id_viagem = int(input(F'{CIAN}\t\t\tDigite o ID da viagem que deseja Excluir: {RESET}'))
    numero_voo = input(F'{CIAN}\t\t\tDigite o número do Vôo. {RESET}')
    destino = input(F'{CIAN}\t\t\tDigite o Destino: {RESET}')
    preco_viagem = float(input(F'{CIAN}\t\t\tDigite o valor da viagem: {RESET}'))
    data = input(F'{CIAN}\t\t\tData e Hora (DD/MM/AAAA 00:00): {RESET}')

    
    cursor.execute("""
        UPDATE dados_viagem 
        SET numero_voo = ?, destino = ?, preco_viagem = ?, data = ?
        WHERE id_viagem = ?
    """, (numero_voo, destino, preco_viagem, data, id_viagem))

    
    print(F'{CIAN}\t\t\tviagem atualizada com sucesso! {RESET}')

    
    conn.commit()
    conn.close()
    
    
    
def excluir_passagem():
    
    conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")
    cursor = conn.cursor()
    
    id_cliente = input(F'{CIAN}\t\t\tDigite o id do titular da passagem: {RESET}')
    cursor.execute("DELETE FROM dados_viagem WHERE id_viagem = ?", (id_cliente,))
    

    print(F'{CIAN}\t\t\tPassagem deletada com sucesso! {RESET}')

    
    conn.commit()
    conn.close()


def exibir_passagens():

    conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dados_viagem")
    resultados = cursor.fetchall()

    os.system('cls')

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