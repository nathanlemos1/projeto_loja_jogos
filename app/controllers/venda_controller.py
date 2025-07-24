def registrar_venda(cliente_id, itens):
	from models.venda_model import Venda
	venda = Venda(cliente_id, itens)
	venda.salvar()

def listar_vendas():
	from models.venda_model import Venda
	return Venda.buscar_todas()

def gerar_relatorio():
	from models.venda_model import Venda
	return Venda.gerar_relatorio()