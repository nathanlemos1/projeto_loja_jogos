import tkinter as tk
from views.cliente_view import ClienteView
from views.produto_view import ProdutoView
from views.venda_view import VendaView
from views.relatorio_view import RelatorioView

class MainView:
    def __init__(self, master):
        self.master = master
        master.title("Nathanos Games - Painel Principal")
        master.geometry("400x350")
        master.configure(bg="#2c2f33")

        tk.Label(master, text="Painel Principal", font=("Segoe UI", 16, "bold"), bg="#2c2f33", fg="white").pack(pady=20)

        tk.Button(master, text="Clientes", width=20, bg="#7289da", fg="white", command=self.abrir_clientes).pack(pady=5)
        tk.Button(master, text="Produtos", width=20, bg="#7289da", fg="white", command=self.abrir_produtos).pack(pady=5)
        tk.Button(master, text="Vendas", width=20, bg="#7289da", fg="white", command=self.abrir_vendas).pack(pady=5)
        tk.Button(master, text="Relatórios", width=20, bg="#7289da", fg="white", command=self.abrir_relatorios).pack(pady=5)
        tk.Button(master, text="Sair", width=20, bg="#99aab5", fg="white", command=master.quit).pack(pady=20)

    def abrir_clientes(self):
        ClienteView(tk.Toplevel(self.master))

    def abrir_produtos(self):
        ProdutoView(tk.Toplevel(self.master))

    def abrir_vendas(self):
        VendaView(tk.Toplevel(self.master))

    def abrir_relatorios(self):
        RelatorioView(tk.Toplevel(self.master))


def abrir_clientes(self):
    print("Abrindo Clientes...")
    ClienteView(tk.Toplevel(self.master))

def abrir_produtos(self):
    print("Abrindo Produtos...")
    ProdutoView(tk.Toplevel(self.master))

def abrir_relatorios(self):
    print("Abrindo Relatórios...")
    RelatorioView(tk.Toplevel(self.master))
