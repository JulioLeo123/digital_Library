from datetime import datetime, timedelta

class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo, prazo_dias):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.prazo_dias = prazo_dias
        self.data_devolucao = data_emprestimo + timedelta(days=prazo_dias)
        self.devolvido = False
        self.data_devolvido = None
        self.multa = 0.0

    def devolver(self, data_devolucao):
        self.devolvido = True
        self.data_devolvido = data_devolucao
        atraso = (data_devolucao - self.data_devolucao).days
        if atraso > 0:
            self.multa = atraso * 1.0
        else:
            self.multa = 0.0
        self.livro.disponibilidade = True
        return self.multa
