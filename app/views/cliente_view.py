import tkinter as tk
from controllers.cliente_controller import cadastrar_cliente, listar_clientes

class ClienteView:
    def __init__(self, master):
        self.master = master
        master.title("Clientes - Nathanos Games")
        master.geometry("400x300")

        tk.Label(master, text="Nome").pack()
        self.nome = tk.Entry(master)
        self.nome.pack()

        tk.Label(master, text="Email").pack()
        self.email = tk.Entry(master)
        self.email.pack()

        tk.Label(master, text="Telefone").pack()
        self.telefone = tk.Entry(master)
        self.telefone.pack()

        tk.Button(master, text="Salvar", command=self.salvar).pack(pady=5)
        self.lista = tk.Text(master, height=10)
        self.lista.pack()
        self.carregar_clientes()

    def salvar(self):
        cadastrar_cliente(self.nome.get(), self.email.get(), self.telefone.get())
        self.carregar_clientes()
    def carregar_clientes(self):
        self.lista.delete('1.0', tk.END)
        for c in listar_clientes():
            self.lista.insert(tk.END, f"{c[0]} - {c[1]} - {c[2]} - {c[3]}\n")