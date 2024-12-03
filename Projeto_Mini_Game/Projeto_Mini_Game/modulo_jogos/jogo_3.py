import random


def jogo_dados():
    
    print('-'*90)
    print()
    print('----------> jOGO DE DADOS <----------')
    print()
    print('Jogue o dado e tente tirar o Maior número para vencer.')
    print()
    
    while True:
        
        dado_sistema = random.randint(1, 6)
        print(f'Computador jogou: {dado_sistema}')
        print()
        
        dado_jogador = input('Aperte "S" para jogar o dado')
        dado_jogador = random.randint(1, 6)
        print(f'Seu Dado: {dado_jogador}')
        
        if dado_jogador > dado_sistema:
            print()
            print('********** PARABÉNS **********')
            print('Você ganhou!!!!')
            print()
        elif dado_jogador == dado_sistema:
            print()
            print('---------> EMPATE <---------')
            print('Tente Novamente...')
            print()
            continue
        else:
            print()
            print('++++++++++ VOCÊ PERDEU ++++++++++')
            print('Tente novamente!!!!')
            print()
            
    return