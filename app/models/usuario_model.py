class Usuario:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
    
    def salvar(self):
        from database.conexao import conectar
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)", (self.usuario, self.senha))
        conn.commit()
        conn.close()
    
    @staticmethod
    def autenticar(usuario, senha):
        from database.conexao import conectar
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
        resultado = cursor.fetchone()
        conn.close()
        return resultado is not None