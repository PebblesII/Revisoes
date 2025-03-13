# 1. Adivinhação de números:
#  • Crie uma lista com 10 números.
#  • Peça ao usuário para adivinhar um número da lista.
#  • Use um loop while para continuar pedindo adivinhações até que o usuário acerte.
import enum
import random
import time
import numpy
import numpy as np
from keras.src.ops import append

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

# media = []
# user2 = 0
# while user2 != "parar":
#      user2 = input("Adicionar um numero a lista:")
#      if user2 != "parar":
#          media.append(user2)
#          print(media)
#
#
#      print("digite parar para parar")
# cal = sum(media) / len(media)
# print(cal)

# 5. Busca em lista:
#  • Crie uma lista de cinco nomes.
#  • Peça ao usuário para digitar um nome.
#  • Usemum loop while para verificar se o nome está na lista e informar o resultado.

# nomes = ["a", "b", "c"]
#
# username = input("Que usario procuras: ")
#
# find = False
# for n in nomes:
#     if n == username:
#         print(f"Usuario achado: {nomes.index(n)}")
#         find = True
#         break
# if find == False:
#     print("Usuario não achado")


# 6. Contador de números:
#  • Solicite ao usuário um número inicial.
#  • Use um loop while para imprimir os números de 1 até o número fornecido pelo usuário.
#  • Exiba uma mensagem indicando que o loop terminou.

# Contar = int(input("Contar até: "))
#
# i = 0
# for n in range(Contar):
#     i += 1
#     print(i)
#     time.sleep(1)
#     if i == Contar:
#         print("End")

# 7. Média de idades
#  • Crie um programa que peça ao usuário que insira idades de pessoas até que ele digite um valor negativo.
#  • Em seguida, utilize um loop while para calcular e exibir a média das idades inseridas.

# idades3 = []
# user = int(input("Idade: "))
# while user > 0:
#     idades3.append(user)
#     print(idades3)
#     user = int(input("Idade: "))
#
#
# media3 = []
# i = 0
# while i < len(idades3):
#     media3 += idades3
#     i += 1
#     print(media3)
# media = sum(media3) / len(idades3)
# print(media)

# 8. Números ímpares
#  • Com a lista numeros = [10, 15, 7, 23, 42, 5, 17, 8, 31, 12, 9, 25, 3, 19, 16, 28, 36, 14, 21, 6], exiba apenas os números ímpares da lista.

# numeros = [10, 15, 7, 23, 42, 5, 17, 8, 31, 12, 9, 25, 3, 19, 16, 28, 36, 14, 21, 6]
#
# i = 0
#
# while i < len(numeros):
#     i += 1
#     if numeros[i] % 2 > 0:
#         print(numeros[i], end=" ")
#     i += 1

# 9. Números primos
#  • Crie um programa que solicite ao usuário que insira números inteiros positivos até que ele digite zero.
#  • Use um loop while para determinar quantos números primos foram inseridos.

# user = int(input(" insira numero: "))
# num = []
#
# while True:
#     if user != 0 and user > 0:
#         num.append(user)
#         print(num)
#         user = int(input(" insira numero: "))
#     else: break
#
# for i in num:
#     if num[i] / 2:
#         print(num[i])

# 10. Remoção de itens
#  • Com a lista nomes = [“Maria”, “José”, “Ana”, “Pedro”, “João”, “Luiza”, “Rafael”, “João”, “Carolina”, “Fernando”], remova todos os nomes “João” da lista e exibam a lista resultante.

# nomes = ["Maria", "José", "Ana", "Pedro", "João", "Luiza", "Rafael", "João", "Carolina", "Fernando"]
# while "João" in nomes:
#     nomes.remove("João")
# print(nomes)

# 11. Calcular
#  • Crie um programa que solicite ao usuário que insira alturas (por exemplo, 1,80 m) de pessoas até que ele digite um valor negativo.
#  • Calcule a média e identifiquem a maior e a menor altura.

# alturas = []
#
# while True:
#     altura = float(input("Altura :"))
#     if altura < 0:break
#     alturas.append(altura)
#     print(alturas)
# media = sum(alturas) / len(alturas)
# print(f"média: {media}, max: {max(alturas)}, min: {min(alturas)}")

# 12. Fatorial
#  • Crie um programa que solicite ao usuário que insira um número inteiro positivo.
#  • use um loop while para calcular e exibir o fatorial desse número.

# num = int(input("Coloque um número: "))
# fatorial = 1
# i = num
#
# while i > 1:
#     fatorial *= i
#     i -= 1
#
# print(fatorial)

