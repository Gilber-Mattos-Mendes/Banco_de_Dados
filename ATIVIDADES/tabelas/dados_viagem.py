import sqlite3
import os


conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_viagem (
        id_viagem INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_voo INTEGER NOT NULL,
        destino TEXT NOT NULL,
        preco_viagem DECIMAL(10, 2),
        data TIMESTAMP
    )
''')
conn.commit()
conn.close()