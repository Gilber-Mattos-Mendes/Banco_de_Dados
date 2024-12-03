import random

def perguntar_capitais(estados_capitais):
    perguntas_corretas = 0

    # Embaralha a lista de estados para tornar o quiz diferente a cada vez
    estados = list(estados_capitais.keys())
    random.shuffle(estados)

    for estado in estados:
        resposta = input(f"Qual é a capital de {estado}? ").strip().title()

        if resposta == estados_capitais[estado]:
            perguntas_corretas += 1
            print("Correto!\n")
        else:
            print(f"Errado! A capital de {estado} é {estados_capitais[estado]}.")
            break

    print(f"\nVocê acertou {perguntas_corretas} perguntas!")
    return

   
    
