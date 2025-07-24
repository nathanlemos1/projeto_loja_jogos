class ItensVenda:
    @staticmethod
    def salvar(venda_id, produto_id, quantidade, conn):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO itens_venda (venda_id, produto_id, quantidade) VALUES (%s, %s, %s)", (venda_id, produto_id, quantidade))    