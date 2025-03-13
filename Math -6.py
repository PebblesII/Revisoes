import random
import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def num_pares():
    pares = []
    contador = 0


    print("-" * 50)
    quantidade = int(input("Digite uma quantidade: "))
    print("-" * 50)

    time.sleep(2)
    
    while contador <= quantidade:
        aleatorio = random.randint(1, 1000)
        if aleatorio % 2 == 0:
            pares.append(aleatorio)
        contador += 1


    print("-" * 50)
    print(pares)
    print("-" * 50)


num_pares()

            
            

            