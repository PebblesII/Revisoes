# TRABALHO: Projeto: Agenda de contatos

# Desenvolva um programa em Python para gerenciar uma agenda de contatos, que deve oferecer as funcionalidades listadas a seguir:

# 1 Adicionar contato: permitir que o usuário adicione novos contatos, fornecendo nome, idade, telefone, e-mail, renda e estado.

# 2 Exibir contatos: mostrar uma lista completa de todos os contatos na agenda, incluindo nome, telefone e e-mail.

# 3 Buscar contato: permitir que o usuário busque as informações de um contato específico, fornecendo o nome do contato.

# 4 Remover contato: possibilitar a remoção de um contato da agenda com base no nome.

# 5 Corrigir contato: substituir uma informação de um contato.

# 6 Mostrar a quantidade de contatos cadastrados.

# 7 Mostrar a média de idade dos contados cadastrados.

# 8 Mostrar a quantidade de contatos cadastrados por estado


#Lembre-se de que o programa deve permitir que o usuário preencha os contatos até digitar “sair”

import os
import time




def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

contantos = {

}


def Adicionar():
    i = 0
    while True:

        username = input("Contanto novo: ")
        userage = input("Idade: ")
        userphone = int(input("Número de telefone: "))
        usermail = input("Email: ")
        userrenda = int(input("Renda: "))
        userstate = input("Estado: ")

        contantos[username] = [f"Idade: {userage}", f"Telephone: {userphone}", f"Email: {usermail}" , f"Renda: {userrenda}", f"Estado: {userstate}" ]

        stop = input("Sair?: [Y] or [N] ")
        if stop == "Y":
            break
        else:
            i+=1
            print(f"Numero de contantos: {i}")
            clear()


def search(username):
    if username in contantos:
        return print(contantos[username])
    else:
        print("Contato inexsitente")


def Corrigir(username):
    if username in contantos:
        qual = int(input("Corrigir oque?: idade [1], Telephone [2], Email [3], Renda [4], Estado [5] "))
        nova = input("Nova informação: ")

        contantos[username][qual - 1] = nova
    else:
        print("Contato inexsitente")

def deletar(username):
    if username in contantos:
        contantos.pop(username)
    else:
        print("Contato inexsitente")

print(contantos)
while True:
    Escolha = input("Oque quer fazer Adicionar [1], Procurar [2], Corrigir [3], Deletar [4] ")
    if Escolha == "1":
        Adicionar()
    elif Escolha == "2":
        search(input("Procurar: "))
    elif Escolha == "3":
        Corrigir(input("Corrigir: "))
    elif Escolha == "4":
        deletar(input("Deletar: "))
