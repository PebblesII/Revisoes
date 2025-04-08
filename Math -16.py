lista = []
print(lista)
lista.append("Ana")
lista.append("Abigail")
print(lista)

tupla = ()
print(tupla)

tupla = ("A", "B")
tupla = list(tupla)
tupla.append("A")
tupla = tuple(tupla)

print(tupla)


conjunto = {}

lista.append("E")
tupla = ("E")
conjunto[0] = "E"

conjunto = {"ana", "abigail", "AAAAAAAA"}
conjunto2 = {"ana", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "EEEEEEEEEEEEEEEEE"}
print(lista)
print(tupla)
print(conjunto)

conjunto2.add("abigail")

for i in lista:
    print(i)

dif = conjunto.difference(conjunto2)
print(dif)


interseao = conjunto.intersection(conjunto2)
print(interseao)

print(conjunto.union(conjunto2))