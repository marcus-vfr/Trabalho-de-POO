from sistema.banco import Banco
from validacao.validacoes import validar_valor, validar_numero_conta


def mostrar_menu():
    print("\n=== SISTEMA BANCARIO ===")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver Saldo")
    print("5 - Histórico de Transação")
    print("0 - Sair")


def main():
    banco = Banco()

    while True:
        mostrar_menu()
        opcao = input("ESCOLHA UMA OPÇÃO: ")

        if opcao == "1":
            print("\n[CRIAR CONTA]")
            nome = input("NOME DO CLIENTE: ")
            tipo = input("TIPO DE CONTA (CORRENTE(cc)/POUPANÇA(cp): ")

            banco.criar_conta(nome, tipo)

        elif opcao == "2":
            print("\n[DEPÓSITO]")
            numero = input("NÚMERO DA CONTA: ")
            valor = float(input("QUANTIA: "))

            banco.depositar(numero, valor)

        elif opcao == "3":
            print("\n[SAQUE]")
            numero = input("NÚMERO DA CONTA: ")
            valor = validar_valor(input("QUANTIA "))
            if valor is None:
                continue

            banco.sacar(numero, valor)

        elif opcao == "4":
            print("\n[VERIFICAR SALDO]")
            numero = input("NÚMERO DA CONTA: ")

            banco.consultar_saldo(numero)

        elif opcao == "5":
            print("\n[HISTÓRICO DE TRANSAÇÃO]")
            numero = input("NÚMERO DA CONTA: ")

            banco.mostrar_historico(numero)

        elif opcao == "0":
            print("SAINDO...")
            break

        else:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")


if __name__ == "__main__":
    main()