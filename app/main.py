import tkinter as tk
from views.login_view import LoginView  # import relativo

def main():
    root = tk.Tk()
    LoginView(root)
    root.mainloop()

if __name__ == '__main__':
    main()
