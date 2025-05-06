valor_1 = 4
valor_2 = 6

valor_3 = 40
valor_4 = 40

def soma(valor_1_para_somar: float, valor_2_para_somar: float) -> float:
    """
    uma funcao simples da soma de valores do tipo float que retorna float
    """
    soma1 = valor_1_para_somar + valor_2_para_somar
    return soma1

valor_5 = soma(valor_1_para_somar=valor_1, valor_2_para_somar=valor_2)
valor_6 = soma(valor_3, valor_4)

print(valor_5)

print(valor_6)