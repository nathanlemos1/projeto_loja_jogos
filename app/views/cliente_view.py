import tkinter as tk
from controllers.cliente_controller import cadastrar_cliente, listar_clientes

class ClienteView:
    def __init__(self, master):
        self.master = master
        master.title("Clientes - Nathanos Games")
        master.geometry("450x400")
        master.configure(bg="#2c2f33")

        tk.Label(master, text="Cadastro de Clientes", bg="#2c2f33", fg="white", font=("Segoe UI", 14, "bold")).pack(pady=10)

        tk.Label(master, text="Nome", bg="#2c2f33", fg="white").pack()
        self.nome = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.nome.pack(pady=2)

        tk.Label(master, text="Email", bg="#2c2f33", fg="white").pack()
        self.email = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.email.pack(pady=2)

        tk.Label(master, text="Telefone", bg="#2c2f33", fg="white").pack()
        self.telefone = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.telefone.pack(pady=2)

        tk.Button(master, text="Salvar Cliente", bg="#7289da", fg="white", activebackground="#5b6eae", command=self.salvar).pack(pady=10)

        self.lista = tk.Text(master, height=10, bg="#23272a", fg="white", insertbackground="white")
        self.lista.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_clientes()

    def salvar(self):
        nome = self.nome.get()
        email = self.email.get()
        telefone = self.telefone.get()
        if nome and email and telefone:
            cadastrar_cliente(nome, email, telefone)
            self.nome.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.telefone.delete(0, tk.END)
            self.carregar_clientes()

    def carregar_clientes(self):
        self.lista.delete('1.0', tk.END)
        try:
            clientes = listar_clientes()
            if not clientes:
                self.lista.insert(tk.END, "Nenhum cliente cadastrado.\n")
            for c in clientes:
                self.lista.insert(tk.END, f"{c[0]} - {c[1]} - {c[2]} - {c[3]}\n")
        except Exception as e:
            self.lista.insert(tk.END, f"Erro ao carregar clientes: {e}\n")
