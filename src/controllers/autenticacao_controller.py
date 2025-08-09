# Importa o serviço de autenticação
from src.services.autenticacao_service import autenticar_usuario, registrar_usuario

def login_controller(dados_login):
	"""
	Recebe os dados de login, chama o serviço de autenticação e retorna o resultado.
	"""
	usuario = autenticar_usuario(dados_login['email'], dados_login['senha'])
	if usuario:
		return {"mensagem": "Login realizado com sucesso", "usuario": usuario}
	else:
		return {"mensagem": "Email ou senha inválidos"}

def registro_controller(dados_registro):
	"""
	Recebe os dados de registro, chama o serviço de registro e retorna o resultado.
	"""
	resultado = registrar_usuario(dados_registro)
	if resultado:
		return {"mensagem": "Usuário registrado com sucesso"}
	else:
		return {"mensagem": "Erro ao registrar usuário"}
