import sqlite3
import os


conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes_cadastrados (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

conn.commit()
conn.close()