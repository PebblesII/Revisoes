
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz)

for i in matriz:
    print(i)


for i in range(3):
    for x in range(3):
        print(matriz[i][x])

for i in matriz:
    for x in i:
        print(x)

