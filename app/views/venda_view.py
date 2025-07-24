import tkinter as tk
from controllers.venda_controller import registrar_venda

class VendaView:
    def __init__(self, master):
        self.master = master
        master.title("Vendas - Nathanos Games")
        master.geometry("400x350")
        self.itens = []

        tk.Label(master, text="ID Cliente").pack()
        self.cliente_id = tk.Entry(master)
        self.cliente_id.pack()

        tk.Label(master, text="ID Produto").pack()
        self.produto_id = tk.Entry(master)
        self.produto_id.pack()

        tk.Label(master, text="Quantidade").pack()
        self.quantidade = tk.Entry(master)
        self.quantidade.pack()

        tk.Button(master, text="Adicionar Item", command=self.adicionar_item).pack()
        tk.Button(master, text="Finalizar Venda", command=self.finalizar).pack(pady=10)

        self.lista = tk.Text(master, height=10)
        self.lista.pack()

    def adicionar_item(self):
        try:
            item = {
                'produto_id': int(self.produto_id.get()),
                'quantidade': int(self.quantidade.get())
            }
            self.itens.append(item)
            self.lista.insert(tk.END, f"Produto {item['produto_id']} - Qtde {item['quantidade']}\n")
        except Exception as e:
            print(f"Erro ao adicionar item: {e}")

    def finalizar(self):
        try:
            registrar_venda(int(self.cliente_id.get()), self.itens)
            self.lista.insert(tk.END, "Venda registrada com sucesso!\n")
            self.itens = []
        except Exception as e:
            print(f"Erro ao registrar venda: {e}")
