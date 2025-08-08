import unittest
from src.services.usuario_service import UsuarioService

class TestAutenticacaoUsuario(unittest.TestCase):
    def setUp(self):
        self.service = UsuarioService()
        self.service.cadastrar_usuario("João Silva Santos", "joao.silva@email.com", "MinhaSenh@123", "Estudante")

    def test_login_sucesso(self):
        usuario, erro = self.service.autenticar("joao.silva@email.com", "MinhaSenh@123")
        self.assertIsNotNone(usuario)
        self.assertIsNone(erro)

    def test_login_incorreto_e_bloqueio(self):
        for senha in ["senha123", "wrong456", "invalid789"]:
            usuario, erro = self.service.autenticar("joao.silva@email.com", senha)
        self.assertIsNone(usuario)
        self.assertEqual(erro, "Conta bloqueada por 15 minutos devido a múltiplas tentativas incorretas")

    def test_login_email_inexistente(self):
        usuario, erro = self.service.autenticar("naoexiste@email.com", "qualquer123")
        self.assertIsNone(usuario)
        self.assertEqual(erro, "Email ou senha incorretos")

if __name__ == "__main__":
    unittest.main()
