import customtkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from tkinter import messagebox as msg
from tkinter import Listbox


janela = None
indice_selecionado = None
agenda = []

def deleter():
    global indice_selecionado
    if indice_selecionado is not None:
        msg.showinfo("Success", f"{agenda} Was Deleted")

        del agenda[indice_selecionado]
        arquivo("w", agenda)
        listabox()
        entry_nome.delete(0, tk.END)
        entry_celular.delete(0, tk.END)
        entry_gmail.delete(0, tk.END)

    else:
        msg.showwarning("Failed", "Select Something")


def editi():
    global indice_selecionado
    if indice_selecionado is not None:
        nome = entry_nome.get()
        cel = entry_celular.get()
        gmail = entry_gmail.get()

        if nome and cel and gmail:
            contato = f"{nome} - {cel} - {gmail}"
            agenda[indice_selecionado] = contato
            arquivo("w", contato)
            listabox()
            entry_nome.delete(0, tk.END)
            entry_celular.delete(0, tk.END)
            entry_gmail.delete(0, tk.END)


    elif not indice_selecionado:
        msg.showwarning("Failed", "Select Something")

def carga():
    global agenda
    agenda = arquivo("r")
    listabox()

def arquivo(op = "r", contato = ""):
    arquivo = "DContatos/Contatos.txt"
    try:
        with open(arquivo, op) as arq:
            if op == "r":
                return arq.readlines()
            elif op == "a":
                arq.write(contato)
            elif op == "w":
                arq.writelines(contato)
    except Exception as ex:
        print(f"Error {ex}")
        return []

def addic():
    # dicionario = {}
    nome = entry_nome.get()
    cel = entry_celular.get()
    gmail = entry_gmail.get()

    if nome and cel and gmail:
        contato = f"{nome} - {cel} - {gmail} \n"
        arquivo("a", contato)


        # dicionario = {"nome": nome, "cel" :  cel, "gmail" : gmail}
        # print(dicionario)
        agenda.append(contato)

        entry_nome.delete(0, tk.END)
        entry_celular.delete(0, tk.END)
        entry_gmail.delete(0, tk.END)


        listabox()

    else:
        n = ""
        c = ""
        g = ""
        if not nome:
            n = "Nome"
        if not cel:
            c = "Celular"
        if not gmail:
            g = "Gmail"

        msg.showwarning("Aviso", f"Faltando: {n} {c} {g}")

def listabox():
    lista.delete(0, tk.END)
    for i in agenda:
        lista.insert(tk.END, str(i))

def selecionar_contato(event):
    global indice_selecionado
    try:
        indice_selecionado = lista.curselection()[0]
        print(indice_selecionado)
    except:
        print("Nada selecionado")

    if indice_selecionado is not None:
        contato = agenda[indice_selecionado].split(" - ")
        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, contato[0])
        entry_celular.delete(0, tk.END)
        entry_celular.insert(0, contato[1])
        entry_gmail.delete(0, tk.END)
        entry_gmail.insert(0, contato[2])


def findic():
    #CTkEntrys
    nome = entry_nome.get().lower().strip()
    cel = entry_celular.get().strip()
    gmail = entry_gmail.get().lower().strip()
    indice = None


    lista.select_clear(0, tk.END)

    #Fiding
    if nome or cel or gmail:
        for i in range(0, lista.size()):
            if nome in lista.get(i).lower().strip():
                indice = i
                break
            elif cel in lista.get(i).strip():
                indice = i
                break
            elif gmail in lista.get(i).lower().strip():
                indice = i
                break

    #Warnings
    elif not nome and cel and gmail:
        msg.showwarning("Error", "Missing Info")

    if indice == None:
        msg.showerror("Error", "unable not find anything")

    print(indice)

    #Selection
    if lista.size() > 0 and indice is not None:
        lista.selection_set(indice)
        lista.activate(indice)
        lista.see(indice)



def interface():
    global entry_nome, entry_celular, entry_gmail, lista
    quadro = tk.CTkFrame(janela)
    quadro.pack(padx=20, pady=(0, 20), fill="both", expand=True)


    #Nome
    label_nome = tk.CTkLabel(quadro, text="Nome:")
    label_nome.pack(padx=20, pady=(10, 0), anchor="w")
    entry_nome = tk.CTkEntry(quadro, width=350)
    entry_nome.pack(padx=20)

    #Celular
    label_celular = tk.CTkLabel(quadro, text="Celular:")
    label_celular.pack(padx=20, pady=(10, 0), anchor="w")
    entry_celular = tk.CTkEntry(quadro, width=350)
    entry_celular.pack(padx=20)

    #Gmail
    label_gmail = tk.CTkLabel(quadro, text="Gmail:")
    label_gmail.pack(padx=20, pady=(10, 0), anchor="w")
    entry_gmail = tk.CTkEntry(quadro, width=350)
    entry_gmail.pack(padx=20, pady=(0, 30))

    #Add/Find

    frame = tk.CTkFrame(quadro)
    frame.pack()
    add = tk.CTkButton(frame, text="Add", width=100, command=addic)
    find = tk.CTkButton(frame, text="Find", width=100, command=findic)
    edit = tk.CTkButton(frame, text="Edit", width=100, command=editi)
    delete = tk.CTkButton(frame, text="Del", width=100, command=deleter)


    add.grid(row=0, column=0, padx=50, pady=10)
    find.grid(row=0, column=1, padx=50, pady=10)
    edit.grid(row=1, column=0, padx=50, pady=10)
    delete.grid(row=1, column=1, padx=50, pady=10)
    #ListBox
    lista = Listbox(quadro, width=50, height=10,
                    font=("Verdana", 16),
                    bg=quadro.cget("fg_color")[1],
                    bd=0)
    lista.pack(pady=(20, 0), )
    lista.bind("<<ListboxSelect>>", selecionar_contato)


def main():

    janela = tk.CTk()
    janela.title("Agenda de Contantos")

    interface()
    carga()
    janela.mainloop()

main()