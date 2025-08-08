from src.models.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.usuarios = []
        self.bloqueios = {}
        self.tentativas = {}

    def cadastrar_usuario(self, nome, email, senha, tipo):
        if any(u.email == email for u in self.usuarios):
            return None, "Email já cadastrado"
        if len(senha) < 8:
            return None, "Senha deve ter no mínimo 8 caracteres"
        usuario = Usuario(nome, email, senha, tipo)
        self.usuarios.append(usuario)
        return usuario, None

    def autenticar(self, email, senha):
        bloqueio = self.bloqueios.get(email)
        if bloqueio and bloqueio > Usuario.agora():
            return None, "Conta bloqueada por tentativas incorretas"
        usuario = next((u for u in self.usuarios if u.email == email), None)
        if not usuario or usuario.senha != senha:
            self.tentativas[email] = self.tentativas.get(email, 0) + 1
            if self.tentativas[email] >= 3:
                self.bloqueios[email] = Usuario.add_minutes(15)
                return None, "Conta bloqueada por 15 minutos devido a múltiplas tentativas incorretas"
            return None, "Email ou senha incorretos"
        self.tentativas[email] = 0
        return usuario, None
