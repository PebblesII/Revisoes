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
    quantidade = int(input("Digite uma quantidade"))
    print("-" * 50)

    
    while contador <= quantidade:
        try:
            aleatorio = random.randint(1, 100)
            