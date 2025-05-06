# 1.Calcular Média de Valores em uma Lista
from typing import List

def calculo_media(valores: List[float]) -> float:
    soma: float = sum(valores)
    quantidade: int = len(valores)
    media = soma / quantidade
    return media

lista_valores = [1,2,3,4,5,6,7,8,8,8,8,9,9]
media_calculada = calculo_media(lista_valores)

print(media_calculada)

# 2.Filtrar Dados Acima de um Limite

def filtrar_dados_acima(valores: List[float], limite: float) -> List[float]:
    valores_acima: List[float] = []
    for valor in valores:
        if valor > limite:
            valores_acima.append(valor)
    return valores_acima

valores_filtrados = filtrar_dados_acima(lista_valores, media_calculada)
print(valores_filtrados)

# 3.Contar Valores Únicos em uma Lista

def contando_valores_unicos(valores: List[float]) -> int:
    distintos = len(set(valores))
    return distintos

total_distinto = contando_valores_unicos(valores_filtrados)
print(total_distinto)

# 4.Converter Celsius para Fahrenheit em uma Lista
temperaturas: List[float] = [30,45,80,90,100]

def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]

temperaturas_convertidas = celsius_para_fahrenheit(temperaturas)
print(temperaturas_convertidas)

# 5.Calcular Desvio Padrão de uma Lista

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

variancia_temperaturas = calcular_desvio_padrao(temperaturas_convertidas)
print(variancia_temperaturas)

# 6.Encontrar Valores Ausentes em uma Sequência

sequencia: List[int] = [1,2,3,5,6,7,10]

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    ausentes_sequencia = list(completo - set(sequencia))
    ausentes_sequencia.sort()
    return ausentes_sequencia

valores_encontrados = encontrar_valores_ausentes(sequencia)
print(valores_encontrados)