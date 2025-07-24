import tkinter as tk
from controllers.venda_controller import gerar_relatorio

class RelatorioView:
    def __init__(self, master):
        self.master = master
        master.title("Relatório de Vendas")
        master.geometry("500x300")

        self.lista = tk.Text(master, height=15)
        self.lista.pack()

        self.carregar_relatorio()

    def carregar_relatorio(self):
        try:
            relatorio = gerar_relatorio()
            self.lista.delete('1.0', tk.END)
            for r in relatorio:
                linha = f"Venda {r[0]} | Cliente: {r[1]} | Data: {r[2]} | Total: R${r[3]:.2f}\n"
                self.lista.insert(tk.END, linha)
        except Exception as e:
            self.lista.insert(tk.END, f"Erro ao gerar relatório: {e}\n")
