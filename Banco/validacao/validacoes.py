def validar_valor(valor_str):
    try:
        valor = float(valor_str)
        if valor <= 0:
            print("O VALOR DEVE SER POSITIVO.")
            return None
        return valor
    except ValueError:
        print("NÚMERO INVÁLIDO.")
        return None


def validar_numero_conta(numero_str):
    if not numero_str.isdigit():
        print("NÚMERO DE CONTA INVÁLIDO.")
        return None
    return int(numero_str)