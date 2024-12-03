import os
import sqlite3


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

def passagens():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()

    numero_voo = int(input('Digite o número do Voo: '))
    destino = input('Destino: ')
    preco = float(input('Preço da viagem: '))
    data = input('Data da viagem: ')

    cursor.execute('''
    INSERT INTO dados_viagem (numero_voo, destino, preco, data)
    VALUES (?, ?)
    ''', (numero_voo, destino, preco, data))

    conn.commit()
    conn.close()