import os
  
classe = 1
nome = 'null'

RED = "\033[31m"
RESET = "\033[0m"


def limpar():
        os.system('cls')        
             
def jogo():
        
        def escolha_de_classe():
                
                global nome
                global classe
                
                limpar()
                print('-'*70)
                print('Escolha sua classe')
                print('-'*70)
                print(RED + '-'*70)
                print('Atençao a escolha de classe afetara as escolhas durante sua jornada!!!')
                print('-'*70)
                print(RESET + '1- Guerreiro, Sao extremamente fortes e sabem lutar muito bem !!!')
                print('2- Arqueiros, sao extremamete ageis !!!')
                print('3- Magos, sao extremamentes inteligentes !!!')
                
                classe = int(input('digite sua escolha: '))
                nome = input('Digite o nome do seu heroi: ')
                inicio()
                return nome, classe
                
                
        def inicio():

                limpar()
                print('-'*70)
                print(f'{nome} foi contratado pelo rei para salvar a princesa, o caminho e traiçoeiro.')
                print('-'*70)
                print('1- caminho da esquerda')
                print('2- caminho da direita')

                escolha = int(input('Digite a sua escolha: '))
                
                if escolha == 1:
                        caminho_esquerda()
                        
                elif escolha == 2:
                        caminho_direita()
                                
        def caminho_esquerda():

                limpar()
                print('-'*70)
                print(f'{nome} escolheu a esquerda, caminhado por um tempo na estrada voce encontrou uma enorme ravina, deve haver um jeito de atravessar a estrada!')
                print('-'*70)
                print('1- Derrubar uma arvore por cima da ravina. ')
                print('2- Descer e escalar a ravina.')
                print('3- Utilizar sipos para atravessar.')

                escolha = int(input('Digite a sua escolha: '))
                
                if escolha == 1 and classe == 3:
                        tigre_dente_de_sabre()
                elif escolha == 2 and classe == 2:
                        tigre_dente_de_sabre()      
                elif escolha == 3 and classe == 1:
                        tigre_dente_de_sabre()
                else:
                        morte()
        
        def ravina():
                
                limpar()
                
                print('-'*70)
                print('')
                print('-'*70)
                
                        
        def tigre_dente_de_sabre():

                limpar()
                
                print('-'*70)
                print(f'{nome} atravessou a ravina e entrou na floresta negra, andando voce viu um enorme tigre dente de sabre.')
                print('ele e maior que os normais e olha que os normais ja sao enormes, maior que tigres.')
                print('-'*70)
                print('1- Furar seu coraçao. ')
                print('2- criar uma isca.')
                print('3- subir as arvores e ir pulando entre elas.')

                escolha = int(input('Digite a sua escolha: '))
                
                if escolha == 1 and classe == 1:
                        tigre_dente_de_sabre()
                elif escolha == 2 and classe == 3:
                        tigre_dente_de_sabre()
                elif escolha == 3 and classe == 2:
                        tigre_dente_de_sabre()
                else:
                        morte()
                        
        def caminho_direita():

                limpar()
                print('-'*70)
                print('Voce escolheu a esquerda, caminhado por um tempo na estrada voce encontrou uma enorme ravina, deve haver um jeito de atravessar a estrada!')
                print('-'*70)
                print('1- Derrubar uma arvore por cima da ravina. ')
                print('2- Descer e escalar a ravina.')
                print('3- Utilizar sipos para atravessar.')

                escolha = int(input('Digite a sua escolha: '))
                
                if escolha == 1 and classe == 3:
                        tigre_dente_de_sabre()
                elif escolha == 2 and classe == 2:
                        tigre_dente_de_sabre()      
                elif escolha == 3 and classe == 1:
                        tigre_dente_de_sabre()
                else:
                        morte()
        
        def morte():
                limpar()
                print(RED + '`'*70)
                print('Voce morreu!!!')
                print('`'*70)
                print('Digite renascer para recomeçar!!!')
                renascer = input ( RESET + 'digite... ')
                
                if renascer == 'renascer':
                        escolha_de_classe()

        if classe > 0:
                escolha_de_classe()

if classe > 0:
        jogo()