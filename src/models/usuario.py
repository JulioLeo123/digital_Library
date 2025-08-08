from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nome, email, senha, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo

    @staticmethod
    def agora():
        return datetime.now()

    @staticmethod
    def add_minutes(minutes):
        return datetime.now() + timedelta(minutes=minutes)
