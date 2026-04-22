from contas.conta import Conta
from operacoes.operacao import Operacao


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= 0:
            print("QUANTIA DE SAQUE INVÁLIDA.")
            return

        if valor > self._saldo:
            print("SALDO INSUFICIENTE (Poupança).")
            return

        self._saldo -= valor
        self._historico.adicionar_operacao(Operacao("SAQUE (CP)", valor))
        print("SAQUE REALIZADO COM SUCESSO (Conta Poupança).")