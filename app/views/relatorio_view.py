import tkinter as tk
from controllers.venda_controller import gerar_relatorio

class RelatorioView:
    def __init__(self, master):
        self.master = master
        master.title("Relatório de Vendas - Nathanos Games")
        master.geometry("500x300")

        self.lista = tk.Text(master, height=15)
        self.lista.pack(padx=10, pady=10)

        self.carregar_relatorio()

    def carregar_relatorio(self):
        self.lista.delete('1.0', tk.END)
        try:
            relatorio = gerar_relatorio()

            if not relatorio:
                self.lista.insert(tk.END, "Nenhuma venda registrada ainda.\n")
                return

            for r in relatorio:
                venda_id, nome_cliente, data_venda, total = r
                linha = f"Venda {venda_id} | Cliente: {nome_cliente} | Data: {data_venda} | Total: R${total:.2f}\n"
                self.lista.insert(tk.END, linha)

        except Exception as e:
            print("Erro ao carregar relatório:", e)
            self.lista.insert(tk.END, "Erro ao gerar relatório.\n")
