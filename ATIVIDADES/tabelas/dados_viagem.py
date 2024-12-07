import sqlite3
import os


conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_viagem (
        id_viagem INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_passageiro TEXT,
        numero_voo INTEGER NOT NULL,
        destino TEXT NOT NULL,
        preco_viagem DECIMAL(10, 2),
        data TEXT
    )
''')
conn.commit()
conn.close()