import os
from modulo_jogos.jogo_1 import adivinhacao
from modulo_jogos.jogo_2 import pedra_papel_tesoura
from modulo_jogos.jogo_3 import jogo_dados
from modulo_jogos.jogo_4 import perguntar_capitais


RESET = '\033[0m'
NEGRITO = '\033[1m'
INVERTIDO = '\033[7m'

os.system('cls')

print('"'*90)
print(f'{NEGRITO} \t \t \t----------> MINI GAME <----------')
print(f'{RESET}"'*90)

while True:
    
    
    print(f'{INVERTIDO}Escolha o jogo que deseja jogar: {RESET}')
    print('1 - Adivinhação')
    print('2 - Pedra, Papel, Tesoura')
    print('3 - Jogo de Dados')
    print('4 - Quiz Capital dos Estados')
    print('5 - Salve a Princesa')
    print('6 - Sair')
    print()
    escolha = input(f'{INVERTIDO}Escolha uma opção de (1 à 6): ')
    
    if escolha == '1':
        adivinhacao()
        break
                
    elif escolha == '2':
        pedra_papel_tesoura()
        break
                
    elif escolha == '3':
        jogo_dados()
        break
     
    elif escolha =='4':
        estados_capitais = {
        "Acre": "Rio Branco",
        "Alagoas": "Maceió",
        "Amapá": "Macapá",
        "Amazonas": "Manaus",
        "Bahia": "Salvador",
        "Ceará": "Fortaleza",
        "Espírito Santo": "Vitória",
        "Goiás": "Goiânia",
        "Maranhão": "São Luís",
        "Mato Grosso": "Cuiabá",
        "Mato Grosso do Sul": "Campo Grande",
        "Minas Gerais": "Belo Horizonte",
        "Pará": "Belém",
        "Paraíba": "João Pessoa",
        "Paraná": "Curitiba",
        "Pernambuco": "Recife",
        "Piauí": "Teresina",
        "Rio de Janeiro": "Rio de Janeiro",
        "Rio Grande do Norte": "Natal",
        "Rio Grande do Sul": "Porto Alegre",
        "Rondônia": "Porto Velho",
        "Roraima": "Boa Vista",
        "Santa Catarina": "Florianópolis",
        "São Paulo": "São Paulo",
        "Sergipe": "Aracaju",
        "Tocantins": "Palmas",
        "Distrito Federal": "Brasília"
    }
        perguntar_capitais(estados_capitais)
        break