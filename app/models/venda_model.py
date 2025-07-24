from datetime import datetime
class Venda:
    def __init__(self, cliente_id, itens):
        self.cliente_id = cliente_id
        self.itens = itens  # lista de dicts {produto_id, quantidade}

    def salvar(self):
        from database.conexao import conectar
        from models.itens_venda_model import ItensVenda
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO vendas (cliente_id, data) VALUES (%s, %s)", (self.cliente_id, datetime.now()))
        venda_id = cursor.lastrowid
        for item in self.itens:
            ItensVenda.salvar(venda_id, item['produto_id'], item['quantidade'], conn)
        conn.commit()
        conn.close()

    @staticmethod
    def buscar_todas():
        from database.conexao import conectar
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vendas")
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    @staticmethod
    def gerar_relatorio():
        from database.conexao import conectar
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT v.id, c.nome, v.data, SUM(i.quantidade * p.preco) AS total FROM vendas v JOIN clientes c ON v.cliente_id = c.id JOIN itens_venda i ON i.venda_id = v.id JOIN produtos p ON p.id = i.produto_id GROUP BY v.id")
        relatorio = cursor.fetchall()
        conn.close()
        return relatorio