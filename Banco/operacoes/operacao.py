from datetime import datetime


class Operacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data = datetime.now()

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y %H:%M:%S')} - {self.tipo}: R$ {self.valor:.2f}"