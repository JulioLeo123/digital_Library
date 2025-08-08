import unittest
from src.services.usuario_service import UsuarioService
from src.services.livro_service import LivroService
from src.services.emprestimo_service import EmprestimoService

class TestEmprestimoService(unittest.TestCase):
    def setUp(self):
        self.usuario_service = UsuarioService()
        self.livro_service = LivroService()
        self.emprestimo_service = EmprestimoService()
        self.usuario, _ = self.usuario_service.cadastrar_usuario("João Silva", "joao@email.com", "MinhaSenh@123", "Estudante")
        self.livro = self.livro_service.adicionar_livro("Clean Code", "Robert C. Martin", "978-0132350884", 2008, "Programação")

    def test_emprestimo_sucesso(self):
        emprestimo, erro = self.emprestimo_service.emprestar_livro(self.usuario, self.livro)
        self.assertIsNotNone(emprestimo)
        self.assertIsNone(erro)
        self.assertFalse(self.livro.disponibilidade)

    def test_emprestimo_limite(self):
        for i in range(3):
            livro = self.livro_service.adicionar_livro(f"Livro {i}", "Autor", f"ISBN{i}", 2020, "Categoria")
            self.emprestimo_service.emprestar_livro(self.usuario, livro)
        novo_livro = self.livro_service.adicionar_livro("Extra", "Autor", "ISBNX", 2021, "Categoria")
        emprestimo, erro = self.emprestimo_service.emprestar_livro(self.usuario, novo_livro)
        self.assertIsNone(emprestimo)
        self.assertEqual(erro, "Limite de empréstimos atingido")

    def test_emprestimo_livro_indisponivel(self):
        self.emprestimo_service.emprestar_livro(self.usuario, self.livro)
        outro_usuario, _ = self.usuario_service.cadastrar_usuario("Maria", "maria@email.com", "Senha1234", "Professor")
        emprestimo, erro = self.emprestimo_service.emprestar_livro(outro_usuario, self.livro)
        self.assertIsNone(emprestimo)
        self.assertEqual(erro, "Livro já emprestado")

    def test_devolucao_com_multa(self):
        emprestimo, _ = self.emprestimo_service.emprestar_livro(self.usuario, self.livro)
        # Simula devolução atrasada (devolve 5 dias após o prazo)
        from datetime import timedelta
        data_atrasada = emprestimo.data_devolucao + timedelta(days=5)
        multa = emprestimo.devolver(data_atrasada)
        self.assertIsNotNone(multa)
        self.assertGreater(multa, 0)
        self.assertTrue(self.livro.disponibilidade)

if __name__ == "__main__":
    unittest.main()
