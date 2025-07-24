import tkinter as tk
from controllers.cliente_controller import cadastrar_cliente, listar_clientes

class ClienteView:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Clientes - Nathanos Games")
        master.geometry("400x350")

        # Campos de entrada
        tk.Label(master, text="Nome").pack()
        self.nome = tk.Entry(master)
        self.nome.pack()

        tk.Label(master, text="Email").pack()
        self.email = tk.Entry(master)
        self.email.pack()

        tk.Label(master, text="Telefone").pack()
        self.telefone = tk.Entry(master)
        self.telefone.pack()

        # Botão de salvar
        tk.Button(master, text="Salvar", command=self.salvar).pack(pady=10)

        # Lista de clientes
        self.lista = tk.Text(master, height=10)
        self.lista.pack()

        # Carrega os clientes ao abrir
        self.carregar_clientes()

    def salvar(self):
        try:
            nome = self.nome.get()
            email = self.email.get()
            telefone = self.telefone.get()

            if not nome or not email or not telefone:
                print("Todos os campos são obrigatórios.")
                return

            cadastrar_cliente(nome, email, telefone)
            self.carregar_clientes()

            self.nome.delete(0, tk.END)
            self.email.delete(0, tk.END)
            self.telefone.delete(0, tk.END)

        except Exception as e:
            print("Erro ao salvar cliente:", e)

    def carregar_clientes(self):
        self.lista.delete('1.0', tk.END)
        try:
            clientes = listar_clientes()
            if not clientes:
                self.lista.insert(tk.END, "Nenhum cliente cadastrado.\n")
            else:
                for c in clientes:
                    self.lista.insert(tk.END, f"{c[0]} - {c[1]} - {c[2]} - {c[3]}\n")
        except Exception as e:
            print("Erro ao carregar clientes:", e)
            self.lista.insert(tk.END, "Erro ao carregar clientes.\n")
