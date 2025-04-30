import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from tkinter import messagebox as msg


janela = None
agenda = []

def addic():
    dicionario = {}
    nome = entry_nome.get()
    cel = entry_celular.get()
    gmail = entry_gmail.get()

    if nome and cel and gmail:
        dicionario = {"nome": nome, "cel" :  cel, "gmail" : gmail}
        print(dicionario)
        agenda.append(dicionario)

        entry_nome.delete(0, tk.END)
        entry_celular.delete(0, tk.END)
        entry_gmail.delete(0, tk.END)

        lista.delete(0, tk.END)
        for i in agenda:
            lista.insert(tk.END, f"{datetime.now().strftime("%d/%m/%y")}  {i["nome"]}-{i["cel"]}-{i["gmail"]}")
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

def findic():
    #Entrys
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
    quadro = tk.Frame(janela)
    quadro.pack(padx=20, pady=(0, 20), fill="both", expand=True)


    #Nome
    label_nome = tk.Label(quadro, text="Nome:")
    label_nome.pack(padx=20, pady=(10, 0), anchor="w")
    entry_nome = tk.Entry(quadro, width=50)
    entry_nome.pack(padx=20)

    #Celular
    label_celular = tk.Label(quadro, text="Celular:")
    label_celular.pack(padx=20, pady=(10, 0), anchor="w")
    entry_celular = tk.Entry(quadro, width=50)
    entry_celular.pack(padx=20)

    #Gmail
    label_gmail = tk.Label(quadro, text="Gmail:")
    label_gmail.pack(padx=20, pady=(10, 0), anchor="w")
    entry_gmail = tk.Entry(quadro, width=50)
    entry_gmail.pack(padx=20)

    #Add/Find

    frame = tk.Frame(quadro)
    frame.pack()
    add = tk.Button(frame, text="Add", width=10, command=addic)
    find = tk.Button(frame, text="Find", width=10, command=findic)

    add.grid(row=0, column=0, padx=10, pady=10)
    find.grid(row=0, column=1, padx=10, pady=10)

    #ListBox
    lista = tk.Listbox(quadro, width=50, height=10)
    lista.pack(pady=(20, 0), )


def main():

    janela = tk.Tk()
    janela.title("Agenda de Contantos")

    interface()

    janela.mainloop()


main()