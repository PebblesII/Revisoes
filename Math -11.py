#  Exercícios
import numpy as np

lista = [8, 20, 50, 40, 1, 43, 32, 29, 47, 12, 9, 4]

#  1. Faça um programa que olhe todos os itens da lista acima e diga quantos deles são ímpares.
for i in lista:
    if i % 2 != 0:
        print(i)


# 2. Com a mesma lista, diga quais deles são pares.
for i in lista:
    if i % 2 == 0:
        print(i)

#  3. Da lista acima, copie todos os elementos em outra lista com o nome nova_lista.
novalista = []

for i in lista:
    novalista.append(i)

#  4. Da lista acima, crie uma nova lista copiando cada elemento em ordem crescente. Obs.: não usar sorted().
sortedlist = []
num = 0

while True:
    for i in novalista:
        if i == num:
            sortedlist.append(i)
    num += 1
    if num == max(novalista):
        break
print(sortedlist)

#  5. Da lista acima, transforme todos os elementos em string.

str(sortedlist)
print(sortedlist)

#  6. Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual à soma dos elementos da lista 1 com os da lista 2, na mesma posição
n1 = [1, 2, 3, 4]
n2 = [1, 2, 3, 4]

for i, num in enumerate(n1):
    ans = n1[i] + n2[i]
    print(f"Index = {i}, Answer = {ans}")

# 7. Faça um programa que, dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.
n1 = [1, 3]
n2 = [1, 3]

for i, num in enumerate(n1):
    ans = n1[i] * n2[i]
    print(f"Index = {i}, Answer = {ans}")

#  8. Faça um programa que peça para o usuário digitar 5 números e, ao final, imprima uma lista com os 5 números digitados pelo usuário (sem converter os números para int ou float).
lu = []
while True:
    user = input("Coloque um numero: ")
    if user != "0":
        lu.append(user)
        print("0 para parar")

    if user == "0":
        break

print(lu)

#  9. Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.

for i in lu:
    float(i)
print(lu)

#  10. Usando listas, faça um programa que peça as 4 notas bimestrais e mostre a média


notas = []
while True:
    user = int(input("Coloque notas 4 : "))
    if user != 0:
        notas.append(user)
        print("0 para parar")

    if user == 0:
        break

media = sum(notas) / len(notas)
print(media)