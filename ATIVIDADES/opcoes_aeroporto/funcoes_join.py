import os
import sqlite3
from prettytable import PrettyTable 



conn = sqlite3.connect("C:\Python\Banco_de_Dados\ATIVIDADES\empresa_aerea.db")
cursor = conn.cursor()


def consultar_pedidos():
    cursor.execute('''
    SELECT
        clientes_cadastrados.nome, clientes_cadastrados.idade,                              
        dados_viagem.numero_voo, dados_viagem.destino, dados_viagem.data                                                               
        FROM
            dados_viagem
        JOIN
            clientes_cadastrados ON dados_viagem.id_cliente = clientes_cadastrados.id_cliente
    ''')
    resultados = cursor.fetchall()
    
    # Criar e formatar a tabela para exibição
    tabela = PrettyTable(
        ['Nome', 'Idade', 'Número do Voo', 'Destino', 'Data'])
    for linha in resultados:
        tabela.add_row(linha)
    print(tabela)