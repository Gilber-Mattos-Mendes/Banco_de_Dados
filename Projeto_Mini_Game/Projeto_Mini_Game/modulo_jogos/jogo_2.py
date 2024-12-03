import random


def pedra_papel_tesoura():
    
    print('-'*90)
    print()
    print('----------> PEDRA, PAPEL, TESOURA <----------')
    print()
    print('Escolha sua arma e tente ganhar do Ghost,' 
            ' o melhor jogador de todos os tempos.')
    print()
    
    opcoes = ['pedra', 'papel', 'tesoura']
    
    while True:
        escolha_usuario = input('Escolha entre (Pedra , Papel ou Tesoura),'
                        ' digite "S" para sair: ').capitalize().lower()
        
        if escolha_usuario == 's':
            print('-'*90)
            print()
            print('Espero que tenha se divertido! Até a próxima.')
            print()
            break
        
        elif escolha_usuario not in opcoes:
            print('-'*90)
            print()
            print('Opção inválida. Tente novamente.')
            print()
            continue
        
        escolha_ghost = random.choice(opcoes)
        print('-'*90)
        print()
        print(f'Ghost escolheu: {escolha_ghost}')
        
        if escolha_ghost == escolha_usuario:
            print('-'*90)
            print()
            print('EMPATE! Tente novamente.')
            print()
        
        elif (escolha_usuario == "Pedra" and escolha_ghost == "Tesoura") or \
                (escolha_usuario == "Papel" and escolha_ghost == "Pedra") or \
                (escolha_usuario == "Tesoura" and escolha_ghost == "Papel"):
                    print('-'*90)
                    print()
                    print('UAU!!!!! ********** PAREBÉNS **********')
                    print()
                    print('Você ganhou!!!!!')
                    print()
                    print('Se você se considera tão bom, tente ganhar novamente!')
                    print()
        else:
            print('-'*90)
            print()
            print('********** VOCÊ PERDEU **********')
            print()
            print('Eu te avisei! Ghost é o melhor de todos os tempos!!1')
            print()
            print('Não desenime, Tente novamente.')
            print()
            
    return