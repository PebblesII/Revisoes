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


print(contantos)


def search(username):
    if username in contantos:
        return print(contantos[username])
    else:
        print("Contanto inexsitente")


procurar = input("Procurar?: [Y] or [N] ")
while True:
    if procurar == "Y":
        Individuo = input("Procurar: ")
        search(Individuo)
        time.sleep(3)
        procurar = input("Procurar?: [Y] or [N] ")
    else:
        break

