# Exercícios
from datetime import datetime as dt

now = dt.now()
currentTime = now.hour

#  1. Escreva uma função que retorne o maior de dois números
def maiorNum(n1, n2):
    if n1 > n2:
        return print(n1)
    else:
        return print(n2)

#  2. Escreva uma função que receba dois números e retorne True, se o primeiro número for múltiplo do segundo.
def Multiplo(n1, n2):
    if n1 % n2 == 0:
        return print("True")
    else:
        return print("False")


#  3. Escreva uma função que receba o lado (l) de um quadrado e retorne sua área (A = lado2).

def quad(l : int):
    if isinstance(l, int): return print(l**2)
    else:
        return print("Error")

#  4. Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura)/2).

def triangle(base : int, altura : int):
    if isinstance(base, int) and isinstance(altura, int):
        A = (base * altura) / 2
        return print(A)
    else:
        print("Error")


#  5. Faça uma função que recebe um nome e imprime “olá, [nome]”.

def HelloName(nome : str):
    if isinstance(nome, str):
        return print(f"olá, {nome}")
    else:
        return print("Error")


#  6. Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”, caso seja antes de 12h; “Boa Tarde, [nome]”, caso seja entre 12h e 18h; e “Boa noite, [nome]” caso seja após às 18h.

def Gooday(Horario : int, Name : str):

    if isinstance(Horario, int) and isinstance(Name, str):
        if Horario > 0 and Horario < 13:
            print(f"Bom dia, {Name}")
        elif Horario > 13 and Horario < 18:
            print(f"Boa tarde, {Name}")
        else:
            print(f"Boa noite, {Name}")
    else:
        print("Error")

Gooday(currentTime, "Gustavo")


#  7. Faça uma função que recebe um número e retorna True, se ele for par, ou False, se ele for ímpar.

def parOuImpar(n1 : int):
    if isinstance(n1, int):
        if n1 % 2 == 0:
            return print("True")
        else:
            print("False")
    else:
        print("Error")



#  8. Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, os números mínimo e máximo de caracteres. Retorne verdadeiro,se o tamanho da string estiver entre os valores de máximo e mínimo, e falso em caso contrário.

def string(string : str):
    if isinstance(string, str):
        a = len(string)
        if a < 10 and a > 2:
            return print("True")
        else:
            return print("False")
    else:
        print("Error")


#  9. Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro, se a string for encontrada dentro da lista, e falso, em caso contrário.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def tanalista(list, num : int):
    if isinstance(num, int):
        for i in list:
            if i == num:
               return print("True")

    else:
        print("Error")

tanalista(list, 3)