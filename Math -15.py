# Estrutura : Listas, tuplas, cojuntos e dicionarios

r = range(1, 9)

print(r)

for i in r:
    print(i)

lista = list(r)

print(lista)

tupla = tuple(r)

print(tupla)

lista.append(9)

print(tupla.index(2))
print(lista.index(2))

conjunto = set(r)
print(conjunto)

conjunto.add(9)

conjunto = {}
conjunto = set()

dic = {
    "sp": "São paulo",
    "rj": "Rio de Janeiro",
    "mj": "Minas Gerais"
}

print(dic["sp"])

