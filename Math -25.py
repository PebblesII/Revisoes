import tkinter as tk


janela = None
def interface():
    rotulo = tk.Label(janela, text="Tarefa")
    rotulo.pack(pady=10, padx=10)

    tarefa = tk.Entry(janela, width=70)
    tarefa.pack(pady=10, padx=10)

    button = tk.Button(janela, text="Send", width=30)
    button.pack(pady=10, padx=30,)

    lista = tk.Listbox(janela, width=35, height=10)
    lista.pack(pady=10, padx=20,)

    buttonC = tk.Button(janela, text="Finish", width=10)
    buttonC.pack(pady=5)

def main():
    janela = tk.Tk()
    janela.title("Gerenciador de Tarefas")
    interface()
    janela.mainloop()

main()