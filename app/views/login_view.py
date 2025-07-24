import tkinter as tk
from controllers.usuario_controller import autenticar_usuario
from views.main_view import MainView

class LoginView:
    def __init__(self, master):
        self.master = master
        master.title("Login - Nathanos Games")
        master.geometry("400x300")
        master.configure(bg="#2c2f33")

        tk.Label(master, text="Bem-vindo à Nathanos Games", bg="#2c2f33", fg="white", font=("Segoe UI", 14, "bold")).pack(pady=15)

        tk.Label(master, text="Usuário", bg="#2c2f33", fg="white").pack()
        self.usuario = tk.Entry(master, bg="#40444b", fg="white", insertbackground="white")
        self.usuario.pack(pady=5)

        tk.Label(master, text="Senha", bg="#2c2f33", fg="white").pack()
        self.senha = tk.Entry(master, show="*", bg="#40444b", fg="white", insertbackground="white")
        self.senha.pack(pady=5)

        tk.Button(master, text="Entrar", bg="#7289da", fg="white", activebackground="#5b6eae", command=self.login).pack(pady=10)
        tk.Button(master, text="Pular Login", bg="#99aab5", fg="white", command=self.pular_login).pack()

        self.mensagem = tk.Label(master, text="", fg="red", bg="#2c2f33")
        self.mensagem.pack(pady=5)

    def login(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        if autenticar_usuario(usuario, senha):
            self.abrir_main_view()
        else:
            self.mensagem.config(text="Usuário ou senha inválidos")

    def pular_login(self):
        self.abrir_main_view()

    def abrir_main_view(self):
        self.master.withdraw()
        janela_principal = tk.Toplevel(self.master)
        MainView(janela_principal)
        janela_principal.grab_set()
