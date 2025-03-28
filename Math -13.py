# MEGASENA

# Faça uma função que retorne números aleatórios para a Megasena.
# O usuário deverá escolher quantos números irá apostar, sendo no mínimo 6 e no máximo 20 números de 1 a 60.
# Lembre-se de que a lista final de escolhas não pode conter um valor repetido.
# Permita que o usuário continue fazendo outros jogos da Megasena até que ele digite 0 (zero) para parar.
# Ao final, mostre quanto o usário deverá pagar conforme o número de jogos e de palpites por jogo, de acordo com os valores abaixo:

# Números Escolhidos	Valor da Aposta
# 6	                  R$ 5,00
# 7	                  R$ 35,00
# 8	                  R$ 140,00
# 9	                  R$ 420,00
# 10	                R$ 1.050,00
# 11	                R$ 2.310,00
# 12	                R$ 4.620,00
# 13	                R$ 8.580,00
# 14	                R$ 15.015,00
# 15	                R$ 25.025,00
# 16	                R$ 40.040,00
# 17	                R$ 61.880,00
# 18	                R$ 92.820,00
# 19	                R$ 135.660,00
# 20	                R$ 193.800,0
import random

pagar = 0
Nums = []
def megasena(quantidade):
    if quantidade > 5 and quantidade < 21:
        for i in range(quantidade):

            aleatorio = random.randint(1, 60)
            Nums.append(aleatorio)
            aleatorio = random.randint(1, 60)

            while aleatorio in Nums:
                aleatorio = random.randint(1, 60)

    elif quantidade < 6:
        print("Quantidade minima é 6")
    elif quantidade > 20:
        print("Quantidade maxima é 20")


preços = {
    "6":                        5,
    "7":	                   35,
    "8":                       140,
    "9":	                   420,
    "10":	                 1.050,
    "11":	                 2.310,
    "12":	                 4.620,
    "13":	                 8.580,
    "14":	                 15.015,
    "15":	                 25.025,
    "16":	                 40.040,
    "17":	                 61.880,
    "18":	                 92.820,
    "19":	                 135.660,
    "20":	                 193.800,
}

while True:
    Nums.clear()
    print("0 para sair")
    print("-" * 50)
    user = int(input("Quantidade de aposta entre 6 e 20: "))

    if user != 0:
     megasena(user)
     print(Nums)
     pagar += int(preços[str(user)])
     print(f"A Pagar: {pagar}R$")
    else:
        break
