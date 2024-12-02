import os
import sqlite3

conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/SQLITE/meu_banco_de_dados.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM clientes")
resultados = cursor.fetchall()

os.system('cls')
for row in resultados:
    print(row)
conn.close()
