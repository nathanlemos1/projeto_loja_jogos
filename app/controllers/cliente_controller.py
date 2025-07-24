def cadastrar_cliente(nome, email, telefone):
    from models.cliente_model import Cliente
    cliente = Cliente(nome, email, telefone)
    cliente.salvar()
        
def listar_clientes():
    from models.cliente_model import Cliente
    return Cliente.buscar_todos()