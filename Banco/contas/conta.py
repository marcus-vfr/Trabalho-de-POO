from historico.historico import Historico
from operacoes.operacao import Operacao


class Conta:
    _contador = 1

    def __init__(self, cliente):
        self._numero = Conta._contador
        Conta._contador += 1

        self._cliente = cliente
        self._saldo = 0.0
        self._historico = Historico()

    def get_numero(self):
        return self._numero

    def get_saldo(self):
        return self._saldo

    def get_cliente(self):
        return self._cliente

    def depositar(self, valor):
        if valor <= 0:
            print("VALOR INVÁLIDO PARA DEPOSITO.")
            return

        self._saldo += valor
        self._historico.adicionar_operacao(Operacao("DEPÓSITO", valor))
        print("DEPÓSITO REALIZADO.")

    def sacar(self, valor):
        if valor <= 0:
            print("VALOR INVÁLIDO PARA SAQUE.")
            return

        if valor > self._saldo:
            print("SALDO INSUFICIENTE.")
            return

        self._saldo -= valor
        self._historico.adicionar_operacao(Operacao("SACAR", valor))
        print("SAQUE FEITO COM SUCESSO.")

    def consultar_saldo(self):
        print(f"SALDO: R$ {self._saldo:.2f}")

    def mostrar_historico(self):
        self._historico.mostrar()