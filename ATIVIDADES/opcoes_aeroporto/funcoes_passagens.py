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
    
    
def atualizar_passagem():

    conn = sqlite3.connect("C:/Repositorios/Banco_de_Dados/ATIVIDADES/empresa_aerea.db")
    cursor = conn.cursor()

    
    nome_cliente = input("Digite o nome do cliente: ")
    nova_idade = int(input("Digite a nova idade: "))

    
    cursor.execute("UPDATE clientes_cadastrados SET idade = ? WHERE nome = ?",
                (nova_idade, nome_cliente))

    
    conn.commit()
    print("Dados atualizados com sucesso!")
    conn.close()