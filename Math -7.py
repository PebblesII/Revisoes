from fontTools.misc.cython import returns
from numpy.ma.core import append
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    print(i, end=" ")

print("for ", "-" * 30)

for i in range(0 , len(lista)):
    print(lista[i], end=" ")

print("Range ", "-" * 30)

lista.clear()

for num in range(0, 11):
    print(num, end=" ")
    lista.append(num)

print("Num ", "-" * 30)

i=0

while i < len(lista):
    print(lista[i], end=" ")
    i+=1

print("While ", "-" * 30)

i=5
for i in range(0, i + 1):
    print(i, end=" ")
    i-=1

print("Reverse ", "-" * 30)

n =  2 #int(input("Digite um inteiro: "))

i=0
while i <= n - 1:
    print(i, end=" ")
    i += 1

print("Number - 1 ", "-" * 30)

Max = lista[0]
for i in lista:

    if i > Max:
        Max = i

print(Max, end=" ")

print("MAX ", "-" * 30)


for i in range(0, 3):
    print(max(lista), end=" ")
    lista.remove(max(lista))

print("- 3 - MAX ", "-" * 30)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



