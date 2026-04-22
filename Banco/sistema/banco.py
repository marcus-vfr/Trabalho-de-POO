from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca
from clientes.cliente import Cliente


class Banco:
    def __init__(self):
        self._contas = {}

    def _buscar_conta(self, numero):
        return self._contas.get(numero)

    def criar_conta(self, nome, tipo):
        cliente = Cliente(nome)

        if tipo.lower() == "cc":
            conta = ContaCorrente(cliente)
        elif tipo.lower() == "cp":
            conta = ContaPoupanca(cliente)
        else:
            print("TIPO INVÁLIDO DE CONTA.")
            return

        self._contas[conta.get_numero()] = conta
        print(f"CONTA CRIADA COM SUCESSO! NÚMERO: {conta.get_numero()}")

    def depositar(self, numero, valor):
        conta = self._buscar_conta(int(numero))

        if not conta:
            print("CONTA NÃO ENCONTRADA.")
            return

        conta.depositar(valor)

    def sacar(self, numero, valor):
        conta = self._buscar_conta(int(numero))

        if not conta:
            print("CONTA NÃO ENCONTRADA.")
            return

        conta.sacar(valor)

    def consultar_saldo(self, numero):
        conta = self._buscar_conta(int(numero))

        if not conta:
            print("CONTA NÃO ENCONTRADA.")
            return

        conta.consultar_saldo()

    def mostrar_historico(self, numero):
        conta = self._buscar_conta(int(numero))

        if not conta:
            print("CONTA NÃO ENCONTRADA.")
            return

        conta.mostrar_historico()