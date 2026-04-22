class Historico:
    def __init__(self):
        self._operacoes = []

    def adicionar_operacao(self, operacao):
        self._operacoes.append(operacao)

    def mostrar(self):
        if not self._operacoes:
            print("NENHUMA TRANSAÇÃO ENCONTRADA.")
            return

        for op in self._operacoes:
            print(op)