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

