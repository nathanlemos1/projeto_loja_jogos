def cadastrar_produto(nome, preco, tipo):
    from models.produto_model import Produto
    produto = Produto(nome, preco, tipo)
    produto.salvar()

def listar_produtos():
    from models.produto_model import Produto
    return Produto.buscar_todos()