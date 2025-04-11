from random import randint as r

tupla = (r(1, 100), r(1, 100), r(1, 100), r(1, 100))
print(tupla)

inteiro = (int(input()))
print(inteiro)
print()

numeross = ()
while True:
    numeros = input()
    if numeros == "s": break
    if numeros.isnumeric():
        numeros = int(numeros)
        if numeros not in numeross:
            numeross += (numeros, )

print(numeross)
print(sorted(numeross))
nova = tuple(sorted(numeross))
print(nova)