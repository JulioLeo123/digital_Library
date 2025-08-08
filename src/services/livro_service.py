from src.models.livro import Livro

class LivroService:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor, isbn, ano, categoria):
        livro = Livro(titulo, autor, isbn, ano, categoria)
        self.livros.append(livro)
        return livro

    def buscar_livros(self, termo=None, categoria=None, ano=None):
        resultados = self.livros
        if termo:
            resultados = [l for l in resultados if termo.lower() in l.titulo.lower() or termo.lower() in l.autor.lower() or termo == l.isbn]
        if categoria:
            resultados = [l for l in resultados if l.categoria == categoria]
        if ano:
            resultados = [l for l in resultados if l.ano == ano]
        return resultados
