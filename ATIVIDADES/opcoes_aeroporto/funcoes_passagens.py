import os
import sqlite3



def adicionar_passagens():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()

    numero_voo = int(input('Digite o número do Voo: '))
    destino = input('Destino: ')
    preco_viagem = float(input('Preço da viagem: '))
    data = input('Data da viagem: ')

    cursor.execute('''
    INSERT INTO dados_viagem (numero_voo, destino, preco_viagem, data)
    VALUES (?, ?)
    ''', (numero_voo, destino, preco_viagem, data))

    conn.commit()
    conn.close()