from random import randint as r
valores = [[], []]



for n in range(r(1, 100)):
    e = r(1, 100)
    if n % 2 == 0:
        valores[0].append(e)
    else:
        valores[1].append(e)


print(sorted(valores[0]))
print(sorted(valores[1]))