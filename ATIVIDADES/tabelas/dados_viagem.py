import sqlite3
import os


conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_viagem (
        id_viagem INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INTEGER NOT NULL,
        id_bagagens INTEGER NOT NULL,
        numero_voo INTEGER NOT NULL,
        destino TEXT NOT NULL,
        preco_viagem DECIMAL(10, 2),
        data TEXT,
        FOREIGN KEY (id_cliente) REFERENCES clientes_cadastrados (id_cliente),
        FOREIGN KEY (id_bagagens) REFERENCES bagagens (id_bagagens)
    )
''')
conn.commit()
conn.close()