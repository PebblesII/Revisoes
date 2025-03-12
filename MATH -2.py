# 1. Adivinhação de números:
#  • Crie uma lista com 10 números.
#  • Peça ao usuário para adivinhar um número da lista.
#  • Use um loop while para continuar pedindo adivinhações até que o usuário acerte.
import enum
import random
import time
import numpy
import numpy as np

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# asw = (num[random.randint(0, 9)])
# print(asw)
# user = int(input("Adivenhe entre 1 a 10: "))
# while user != asw:
#     user = int(input("Errado tente novamente: "))

# 2. Contagem regressiva:
#  • Crie uma lista de contagem regressiva de 10 a 1.
#  • Use um loop while para imprimir cada número da lista.

# regressiva = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = len(regressiva)
# while x >= 1:
#     x -= 1
#     print(regressiva)
#     regressiva.pop(-1)
#     time.sleep(1)

# 3. Adição de números:
#  • Crie uma lista vazia para armazenar números.
#  • Peça ao usuário para fornecer números e os adicionem à lista.
#  • Continue pedindo números até que o usuário decida parar.

# adc = []
# user1 = 0
# while user1 != "parar":
#     user1 = input("Adicionar um numero a lista:")
#     adc.append(user1)
#     print(adc)
#     print("digite parar para parar")

# 4. Média de notas:
#  • Crie uma lista vazia para armazenar notas.
#  • Peça ao usuário para fornecer notas e as adicionem à lista.
#  • Calcule e imprima a média das notas quando o usuário decidir parar.

media = []
user2 = 0
while user2 != "parar":
    user2 = input("Adicionar um numero a lista:")
    if user2 != "parar":
        media.append(user2)
        print(media)


    print("digite parar para parar")
cal = max(media) - min(media)
print(cal)

# 5. Busca em lista:
#  • Crie uma lista de cinco nomes.
#  • Peça ao usuário para digitar um nome.
#  • Usemum loop while para verificar se o nome está na lista e informar o resultado.


# 6. Contador de números:
#  • Solicite ao usuário um número inicial.
#  • Use um loop while para imprimir os números de 1 até o número fornecido pelo usuário.
#  • Exiba uma mensagem indicando que o loop terminou.


# 7. Média de idades
#  • Crie um programa que peça ao usuário que insira idades de pessoas até que ele digite um valor negativo.
#  • Em seguida, utilize um loop while para calcular e exibir a média das idades inseridas.


# 8. Números ímpares
#  • Com a lista numeros = [10, 15, 7, 23, 42, 5, 17, 8, 31, 12, 9, 25, 3, 19, 16, 28, 36, 14, 21, 6], exiba apenas os números ímpares da lista.


# 9. Números primos
#  • Crie um programa que solicite ao usuário que insira números inteiros positivos até que ele digite zero.
#  • Use um loop while para determinar quantos números primos foram inseridos.


# 10. Remoção de itens
#  • Com a lista nomes = [“Maria”, “José”, “Ana”, “Pedro”, “João”, “Luiza”, “Rafael”, “João”, “Carolina”, “Fernando”], remova todos os nomes “João” da lista e exibam a lista resultante.


# 11. Calcular
#  • Crie um programa que solicite ao usuário que insira alturas (por exemplo, 1,80 m) de pessoas até que ele digite um valor negativo.
#  • Calcule a média e identifiquem a maior e a menor altura.


# 12. Fatorial
#  • Crie um programa que solicite ao usuário que insira um número inteiro positivo.
#  • use um loop while para calcular e exibir o fatorial desse número.