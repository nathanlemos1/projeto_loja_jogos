import tkinter as tk
from controllers.produto_controller import cadastrar_produto, listar_produtos

class ProdutoView:
    def __init__(self, master):
        self.master = master
        master.title("Produtos - Nathanos Games")
        master.geometry("400x300")

        tk.Label(master, text="Nome").pack()
        self.nome = tk.Entry(master)
        self.nome.pack()

        tk.Label(master, text="Preço").pack()
        self.preco = tk.Entry(master)
        self.preco.pack()

        tk.Label(master, text="Tipo (Físico/Digital)").pack()
        self.tipo = tk.Entry(master)
        self.tipo.pack()

        tk.Button(master, text="Salvar", command=self.salvar).pack(pady=5)
        self.lista = tk.Text(master, height=10)
        self.lista.pack()
        self.carregar_produtos()

    def salvar(self):
        cadastrar_produto(self.nome.get(), float(self.preco.get()), self.tipo.get())
        self.carregar_produtos()
    def carregar_produtos(self):
        self.lista.delete('1.0', tk.END)
        for p in listar_produtos():
            self.lista.insert(tk.END, f"{p[0]} - {p[1]} - R${p[2]} - {p[3]}\n")