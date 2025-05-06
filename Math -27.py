import os
cores = open("Cores.txt", "w+")



coreslista = ["azul", "Vermelho", "laranja"]

with open("Cores.txt", "w+") as cores:
    for i in coreslista:
        cores.write(i + "\n")

with open("Cores.txt", "r") as cores:
    print(cores.read())

with open("Cores.txt", "a") as cores:
    cores.write("branco \n")

with open("Cores.txt", "a") as cores:
    novacores = ["a", "b"]
    for i in novacores:
        cores.write(i + "\n")



os.startfile("Cores.txt")
