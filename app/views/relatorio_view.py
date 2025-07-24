import tkinter as tk
from controllers.venda_controller import gerar_relatorio

class RelatorioView:
    def __init__(self, master):
        self.master = master
        master.title("Relatório de Vendas - Nathanos Games")
        master.geometry("500x350")
        master.configure(bg="#2c2f33")

        tk.Label(master, text="Relatório de Vendas", font=("Segoe UI", 14, "bold"), bg="#2c2f33", fg="white").pack(pady=10)

        self.lista = tk.Text(master, height=15, bg="#23272a", fg="white", insertbackground="white")
        self.lista.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_relatorio()

    def carregar_relatorio(self):
        self.lista.delete('1.0', tk.END)
        try:
            relatorio = gerar_relatorio()
            if not relatorio:
                self.lista.insert(tk.END, "Nenhuma venda registrada.\n")
            else:
                for r in relatorio:
                    venda_id, nome_cliente, data_venda, total = r
                    linha = f"Venda {venda_id} | Cliente: {nome_cliente} | Data: {data_venda} | Total: R${total:.2f}\n"
                    self.lista.insert(tk.END, linha)
        except Exception as e:
            self.lista.insert(tk.END, f"Erro ao carregar relatório: {e}\n")
