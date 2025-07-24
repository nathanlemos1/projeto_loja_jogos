class Produto:
    def __init__(self, nome, preco, tipo):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
    
    def salvar(self):
        from database.conexao import conectar
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, tipo) VALUES (%s, %s, %s)", (self.nome, self.preco, self.tipo))
        conn.commit()
        conn.close()
    
    @staticmethod
    def buscar_todos():
        from database.conexao import conectar
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        resultados = cursor.fetchall()
        conn.close()
        return resultados