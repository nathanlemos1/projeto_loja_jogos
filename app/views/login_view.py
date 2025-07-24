import tkinter as tk
from controllers.usuario_controller import autenticar_usuario
from views.main_view import MainView

class LoginView:
    def __init__(self, master):
        self.master = master
        master.title("Login - Nathanos Games")
        master.geometry("300x200")

        tk.Label(master, text="Usuário").pack()
        self.usuario = tk.Entry(master)
        self.usuario.pack()

        tk.Label(master, text="Senha").pack()
        self.senha = tk.Entry(master, show="*")
        self.senha.pack()

        tk.Button(master, text="Entrar", command=self.login).pack(pady=10)
        tk.Button(master, text="Pular Login", command=self.pular_login).pack()

        self.mensagem = tk.Label(master, text="", fg="red")
        self.mensagem.pack()

    def login(self):
        usuario = self.usuario.get()
        senha = self.senha.get()
        if autenticar_usuario(usuario, senha):
            self.master.withdraw()  # Oculta a janela de login
            MainView(tk.Toplevel(self.master))  # Abre o painel principal
        else:
            self.mensagem.config(text="Usuário ou senha inválidos")

    def pular_login(self):
        self.master.withdraw()  # Oculta a janela de login
        MainView(tk.Toplevel(self.master))  # Abre o painel principal sem autenticar
