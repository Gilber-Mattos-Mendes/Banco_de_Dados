import sqlite3
import os


conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bagagens (
        id_bagagens INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_bagagem INTEGER NOT NULL,
        numero_voo INTEGER NOT NULL,
        destino TEXT NOT NULL
    )
''')
conn.commit()
conn.close()