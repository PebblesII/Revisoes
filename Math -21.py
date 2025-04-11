lista = []
while True:
    valor = input()
    if valor == "s": break
    if valor.isnumeric():
        valor = int(valor)
        if valor not in lista:
            if len(lista) == 0 or valor > lista[-1]: lista.append(valor)
            else:
                indice = 0
                while indice < len(lista):
                    if valor < lista[indice]:
                        lista.insert(indice, valor)
                        break
                    else:
                        indice += 1
    print(lista)