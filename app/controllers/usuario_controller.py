def autenticar_usuario(usuario, senha):
    from models.usuario_model import Usuario
    return Usuario.autenticar(usuario, senha)

def cadastrar_usuario(usuario, senha):
    from models.usuario_model import Usuario
    novo = Usuario(usuario, senha)
    novo.salvar()