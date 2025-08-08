class Livro:
    def __init__(self, titulo, autor, isbn, ano, categoria, disponibilidade=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano = ano
        self.categoria = categoria
        self.disponibilidade = disponibilidade

    def detalhes(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "isbn": self.isbn,
            "ano": self.ano,
            "categoria": self.categoria,
            "disponibilidade": self.disponibilidade
        }
