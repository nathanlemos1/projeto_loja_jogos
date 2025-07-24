import tkinter as tk
from controllers.venda_controller import registrar_venda

class VendaView:
    def __init__(self, master):
        self.master = master
        master.title("Registrar Venda - Nathanos Games")
        master.geometry("450x400")
        master.configure(bg="#2c2f33")

        tk.Label(master, text="Registrar Venda", font=("Segoe UI", 14, "bold"), bg="#2c2f33", fg="white").pack(pady=10)

        tk.Label(master, text="ID do Cliente", bg="#2c2f33", fg="white").pack()
        self.cliente_id = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.cliente_id.pack(pady=2)

        tk.Label(master, text="ID do Produto", bg="#2c2f33", fg="white").pack()
        self.produto_id = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.produto_id.pack(pady=2)

        tk.Label(master, text="Quantidade", bg="#2c2f33", fg="white").pack()
        self.quantidade = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.quantidade.pack(pady=2)

        tk.Button(master, text="Registrar Venda", bg="#7289da", fg="white", activebackground="#5b6eae", command=self.registrar).pack(pady=10)

        self.mensagem = tk.Label(master, text="", bg="#2c2f33", fg="white")
        self.mensagem.pack(pady=5)

    def registrar(self):
        try:
            cliente_id = int(self.cliente_id.get())
            produto_id = int(self.produto_id.get())
            quantidade = int(self.quantidade.get())
            cadastrar_venda(cliente_id, produto_id, quantidade)
            self.mensagem.config(text="Venda registrada com sucesso!", fg="green")
            self.cliente_id.delete(0, tk.END)
            self.produto_id.delete(0, tk.END)
            self.quantidade.delete(0, tk.END)
        except Exception as e:
            self.mensagem.config(text=f"Erro: {e}", fg="red")
