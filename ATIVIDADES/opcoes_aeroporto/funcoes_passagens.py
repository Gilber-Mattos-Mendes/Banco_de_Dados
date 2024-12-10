import os
import sqlite3
from prettytable import PrettyTable 
 


def adicionar_passagens():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()

    numero_voo = int(input('Digite o número do Voo: '))
    destino = input('Destino: ')
    preco_viagem = float(input('Preço da viagem: '))
    data = input('Data da viagem: ')

    cursor.execute('''
    INSERT INTO dados_viagem (numero_voo, destino, preco_viagem, data)
    VALUES (?, ?, ?, ?)
    ''', (numero_voo, destino, preco_viagem, data))

    conn.commit()
    conn.close()
    
    
    
    
def atualizar_passagem():
    
    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()
    
    
    id_viagem = int(input('Digite o ID da passagem que deseja Excluir: '))
    numero_voo = input('Digite o número do Vôo. ')
    destino = input('Digite o Destino: ')
    preco_viagem = float(input('Digite o valor da passagem: '))
<<<<<<< HEAD
    data = input('Data e Hora (DD/MM/AAAA 00:00): ')
=======
    data = input('Data e Hora (AAAA/MM/DD 12:35): ')
>>>>>>> 1a5217f6b3f0e81f4f06ef33e310390bb06ba5c6
    
    cursor.execute("""
        UPDATE dados_viagem 
        SET numero_voo = ?, destino = ?, preco_viagem = ?, data = ?
        WHERE id_viagem = ?
    """, (numero_voo, destino, preco_viagem, data, id_viagem))
<<<<<<< HEAD

=======
    
    print('Passagem atualizada com sucesso!')
>>>>>>> 1a5217f6b3f0e81f4f06ef33e310390bb06ba5c6
    
    conn.commit()
    conn.close()
    
    
    
def excluir_passagem():
    
    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()
    
    id_cliente = input('Digite o id do titular da passagem: ')
    cursor.execute("DELETE FROM dados_viagem WHERE id_viagem = ?", (id_cliente,))
    
<<<<<<< HEAD
=======
    print('Passagem deletada com sucesso!')
>>>>>>> 1a5217f6b3f0e81f4f06ef33e310390bb06ba5c6
    
    conn.commit()
    conn.close()


def exibir_passagens():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
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