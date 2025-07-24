import tkinter as tk
from controllers.venda_controller import gerar_relatorio
class RelatorioView:
    def __init__(self, master):
        self.master = master
        master.title("Relatório de Vendas")
        master.geometry("500x300")
        self.lista = tk.Text(master)
        self.lista.pack()
        self.carregar_relatorio()
    def carregar_relatorio(self):
        relatorio = gerar_relatorio()
        for r in relatorio:
            self.lista.insert(tk.END, f"Venda {r[0]} - Cliente: {r[1]} - Data: {r[2]} - Total: R${r[3]:.2f}\n")