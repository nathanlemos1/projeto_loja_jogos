import tkinter as tk
from tkinter import messagebox
from controllers.usuario_controller import autenticar_usuario

class LoginView:
    def __init__(self, master):
        self.master = master
        master.title("Login - Nathanos Games")
        master.geometry("300x180")
        
        tk.Label(master, text="Usuário:").pack(pady=5)
        self.usuario_entry = tk.Entry(master)
        self.usuario_entry.pack()
        
        tk.Label(master, text="Senha:").pack(pady=5)
        self.senha_entry = tk.Entry(master, show="*")
        self.senha_entry.pack()
        
        tk.Button(master, text="Entrar", command=self.login).pack(pady=10)
    
    def login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        if autenticar_usuario(usuario, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            from views.main_view import MainView
            self.master.destroy()
            root = tk.Tk()
            MainView(root)
            root.mainloop()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")