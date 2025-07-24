class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def salvar(self):
        from database.conexao import conectar
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)", (self.nome, self.email, self.telefone))
        conn.commit()
        conn.close()
    
    @staticmethod
    def buscar_todos():
        from database.conexao import conectar
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        resultados = cursor.fetchall()
        conn.close()
        return resultados