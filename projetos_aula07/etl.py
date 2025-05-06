import csv

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Funcao que ler um arquivo csv e retorna uma lista de dicionarios
    """
    dados = []
    with open(nome_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            dados.append(linha)
    return dados

def filtrar_produtos_nao_entregues(dados: str) -> list[dict]:
    """
    Funcao que filtra produtos igual a True
    """
    lsita_com_produtos_filtrados = []
    for dado in dados:
        if dado.get("entregue") == "True":
            lsita_com_produtos_filtrados.append(dado)
    return lsita_com_produtos_filtrados

def somar_valores_dos_produtos(dados: str) -> int:
    """
    Funcao que filtra produtos igual a True
    """
    valor_total = 0
    for dado in dados:
        valor_total += int(dado.get("price"))
    return valor_total