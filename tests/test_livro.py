import unittest
from src.services.livro_service import LivroService

class TestLivroService(unittest.TestCase):
    def setUp(self):
        self.service = LivroService()
        self.service.adicionar_livro("Clean Code", "Robert C. Martin", "978-0132350884", 2008, "Programação")
        self.service.adicionar_livro("Python Fluente", "Luciano Ramalho", "978-8575225636", 2015, "Programação")

    def test_busca_por_titulo(self):
        resultados = self.service.buscar_livros(termo="Clean Code")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].titulo, "Clean Code")

    def test_busca_por_autor(self):
        resultados = self.service.buscar_livros(termo="Luciano Ramalho")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].autor, "Luciano Ramalho")

    def test_busca_por_isbn(self):
        resultados = self.service.buscar_livros(termo="978-0132350884")
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].isbn, "978-0132350884")

    def test_filtro_categoria(self):
        resultados = self.service.buscar_livros(categoria="Programação")
        self.assertEqual(len(resultados), 2)

    def test_filtro_ano(self):
        resultados = self.service.buscar_livros(ano=2015)
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0].ano, 2015)

if __name__ == "__main__":
    unittest.main()
