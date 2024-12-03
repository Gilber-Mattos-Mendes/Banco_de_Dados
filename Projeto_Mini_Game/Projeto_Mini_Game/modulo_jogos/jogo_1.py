
import random


def adivinhacao():
    
    print('-'*90)
    print()
    print('----------> jOGO DE ADIVINHAÇÃO <----------')
    print()
    print('Adivinhe o número de 1 a 50.')
    print()
    numero_certo = random.randint(1, 50)
    
        
    for c in range(9): 
        tentativa_user = int(input('O número é: '))
        c += 1
        
        if c == 9:
            print('Você perdeu! Volte e tente novamente.')
            print()
            
        elif numero_certo > tentativa_user:
            print('Errou! Tente um número maior.') 
            
        elif numero_certo < tentativa_user:
            print('Errou! Tente um número menor.')
            
        else:
            print()
            print('*************** PARABÉNS ***************')
            print(f'Você acertou!!!!!')
            print(f' Número correto {numero_certo}')
            
    return