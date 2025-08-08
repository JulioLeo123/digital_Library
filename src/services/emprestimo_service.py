from src.models.emprestimo import Emprestimo
from datetime import datetime

class EmprestimoService:
    def __init__(self):
        self.emprestimos = []

    def pode_emprestar(self, usuario):
        ativos = [e for e in self.emprestimos if e.usuario.email == usuario.email and not e.devolvido]
        return len(ativos) < 3

    def emprestar_livro(self, usuario, livro):
        if not livro.disponibilidade:
            return None, "Livro já emprestado"
        if not self.pode_emprestar(usuario):
            return None, "Limite de empréstimos atingido"
        prazo = 7 if usuario.tipo == "Estudante" else 14 if usuario.tipo == "Professor" else 7
        emprestimo = Emprestimo(usuario, livro, datetime.now(), prazo)
        livro.disponibilidade = False
        self.emprestimos.append(emprestimo)
        return emprestimo, None

    def devolver_livro(self, usuario, livro):
        for e in self.emprestimos:
            if e.usuario.email == usuario.email and e.livro.isbn == livro.isbn and not e.devolvido:
                multa = e.devolver(datetime.now())
                return multa
        return None
