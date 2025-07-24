import tkinter as tk
from views.cliente_view import ClienteView
from views.produto_view import ProdutoView
from views.venda_view import VendaView
from views.relatorio_view import RelatorioView

class MainView:
    def __init__(self, master):
        self.master = master
        master.title("Nathanos Games - Painel Principal")
        master.geometry("400x300")
        
        tk.Button(master, text="Clientes", command=self.abrir_clientes).pack(pady=5)
        tk.Button(master, text="Produtos", command=self.abrir_produtos).pack(pady=5)
        tk.Button(master, text="Vendas", command=self.abrir_vendas).pack(pady=5)
        tk.Button(master, text="Relatórios", command=self.abrir_relatorios).pack(pady=5)
        tk.Button(master, text="Sair", command=master.quit).pack(pady=20)

    def abrir_clientes(self):
        ClienteView(tk.Toplevel(self.master))
    def abrir_produtos(self):
        ProdutoView(tk.Toplevel(self.master))
    def abrir_vendas(self):
        VendaView(tk.Toplevel(self.master))
    def abrir_relatorios(self):
        RelatorioView(tk.Toplevel(self.master))