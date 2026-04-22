from contas.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, cliente, limite=500):
        super().__init__(cliente)
        self._limite = limite

    def sacar(self, valor):
        if valor <= 0:
            print("QUANTIA INVÁLIDA PARA SAQUE.")
            return

        if valor > self._saldo + self._limite:
            print("LIMITE EXCEDIDO.")
            return

        self._saldo -= valor
        self._historico.adicionar_operacao(
            __import__("operacoes.operacao").operacao.Operacao("SAQUE (CC)", valor)
        )
        print("SAQUE FEITO COM SUCESSO (Conta Corrente).")