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

