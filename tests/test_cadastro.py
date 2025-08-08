import unittest
from src.services.usuario_service import UsuarioService

class TestCadastroUsuario(unittest.TestCase):
    def setUp(self):
        self.service = UsuarioService()

    def test_cadastro_valido(self):
        usuario, erro = self.service.cadastrar_usuario("João Silva Santos", "joao.silva@email.com", "MinhaSenh@123", "Estudante")
        self.assertIsNotNone(usuario)
        self.assertIsNone(erro)
        self.assertEqual(usuario.email, "joao.silva@email.com")

    def test_email_duplicado(self):
        self.service.cadastrar_usuario("Teste", "teste@email.com", "Senha1234", "Professor")
        usuario, erro = self.service.cadastrar_usuario("Maria Oliveira", "teste@email.com", "OutraSenh@456", "Professor")
        self.assertIsNone(usuario)
        self.assertEqual(erro, "Email já cadastrado")

    def test_senha_curta(self):
        usuario, erro = self.service.cadastrar_usuario("Teste", "novo@email.com", "1234567", "Estudante")
        self.assertIsNone(usuario)
        self.assertEqual(erro, "Senha deve ter no mínimo 8 caracteres")

if __name__ == "__main__":
    unittest.main()
