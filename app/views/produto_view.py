import tkinter as tk
from controllers.produto_controller import cadastrar_produto, listar_produtos

class ProdutoView:
    def __init__(self, master):
        self.master = master
        master.title("Produtos - Nathanos Games")
        master.geometry("450x400")
        master.configure(bg="#2c2f33")

        tk.Label(master, text="Cadastro de Produtos", bg="#2c2f33", fg="white", font=("Segoe UI", 14, "bold")).pack(pady=10)

        tk.Label(master, text="Nome", bg="#2c2f33", fg="white").pack()
        self.nome = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.nome.pack(pady=2)

        tk.Label(master, text="Preço", bg="#2c2f33", fg="white").pack()
        self.preco = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.preco.pack(pady=2)

        tk.Label(master, text="Tipo (Físico/Digital)", bg="#2c2f33", fg="white").pack()
        self.tipo = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.tipo.pack(pady=2)

        tk.Button(master, text="Salvar Produto", bg="#7289da", fg="white", activebackground="#5b6eae", command=self.salvar).pack(pady=10)

        self.lista = tk.Text(master, height=10, bg="#23272a", fg="white", insertbackground="white")
        self.lista.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_produtos()

    def salvar(self):
        nome = self.nome.get()
        preco = self.preco.get()
        tipo = self.tipo.get()
        if nome and preco and tipo:
            try:
                cadastrar_produto(nome, float(preco), tipo)
                self.nome.delete(0, tk.END)
                self.preco.delete(0, tk.END)
                self.tipo.delete(0, tk.END)
                self.carregar_produtos()
            except Exception as e:
                print("Erro ao salvar produto:", e)

    def carregar_produtos(self):
        self.lista.delete('1.0', tk.END)
        try:
            produtos = listar_produtos()
            if not produtos:
                self.lista.insert(tk.END, "Nenhum produto cadastrado.\n")
            for p in produtos:
                self.lista.insert(tk.END, f"{p[0]} - {p[1]} - R${p[2]:.2f} - {p[3]}\n")
        except Exception as e:
            self.lista.insert(tk.END, f"Erro ao carregar produtos: {e}\n")
