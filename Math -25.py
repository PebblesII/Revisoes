import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter import messagebox as msg
tarefa = lista = lista = None
tarefas = []

answear = None

def Adicionar():
    adicionar = tarefa.get()
    if adicionar:
        tarefas.append(adicionar)
        lista.insert(tk.END, f"{datetime.now().strftime("%d/%m")} {adicionar}")
        print(tarefas)
    else:
        msg.showwarning("Error", "Type something")
        answear = msg.askquestion("BLEHHHHHHHHHHHHHHHHHHH", "Do u wan die")

def finsish():
    item = lista.curselection()
    if item:
        concluida = tarefas.pop(item[0])
        lista.delete(item)
        msg.showinfo("Success", f"{concluida} Was Deleted")
    else:
        msg.showwarning("Failed", "Select Something")

def interface():
    global tarefa, lista

    rotulo = tk.Label(janela, text="Tarefa")
    rotulo.pack(pady=10, padx=10)

    tarefa = tk.Entry(janela, width=70)
    tarefa.pack(pady=10, padx=10)

    button = tk.Button(janela, text="Send",command=Adicionar, width=30)
    button.pack(pady=10, padx=30,)

    lista = tk.Listbox(janela, width=35, height=10)
    lista.pack(pady=10, padx=20,)

    buttonC = tk.Button(janela, text="Finish", command=finsish, width=10)
    buttonC.pack(pady=5)

def main():
    global janela

    janela = tk.Tk()
    janela.title("Gerenciador de Tarefas")
    interface()
    janela.mainloop()

main()