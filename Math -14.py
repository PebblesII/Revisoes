# Exercícios
from operator import index

#  1. Crie duas variáveis do tipo string, uma contendo “Olá” e outra contendo “Mundo”. Concatene-as e imprima o resultado.
ola = "ola "
mundo = "mundo"
print(ola + mundo)


#  2. Dada a string “Python”, imprima o caractere que está no índice 2.


#  3. Crie uma string qualquer. Substitua um dos caracteres por outro e imprima a nova string resultante.

#  4. Solicite ao usuário que digite seu nome. Em seguida, imprima o comprimento do nome fornecido.

#  5. Crie uma string que represente uma frase. Verifique se a palavra “gato” está presente na frase e imprima o resultado (verdadeiro ou falso)

#  6. Peça ao usuário que digite uma frase. Conte o número de palavras na frase e imprima o resultado.

#  7. Crie uma função que receba uma frase como parâmetro e retorne a mesma frase com as palavras invertidas. Por exemplo, “Olá Mundo” deve ser transformado em “Mundo Olá”.

#  8. Solicite ao usuário que digite uma string que contenha espaços em branco no início e no final. Remova esses espaços e imprima a string resultante.

#  9. Crie uma função que receba um número inteiro e retorne uma string que o represente com separadores de milhares. Por exemplo, para o número 1234567, a função deve retornar “1,234,567”.

#  10. Implemente uma função que receba uma string e um número (chamado de “deslocamento”) como parâmetros e retorne a string cifrada, usando a Cifra de César. Cada letra na string deve ser deslocada pelo número fornecido. Por exemplo, com um deslocamento de 3, “ABC” seria cifrado como “DEF”
# def cifra(string : str, deslocamento):
#     resultado = ""
#     for i in string:
#         if i.isalpha():
#             base = 65 if i.isupper() else 97
#             resultado += i((ord(i)) - deslocamento + base) % 26 + base)
#         else:
#             resultado += i
#     return resultado


# 11. Escreva um programa que receba uma palavra ou frase do usuário e determine se ela é um palíndromo ou não. O programa deve ignorar maiúsculas e minúsculas, bem como espaços em branco