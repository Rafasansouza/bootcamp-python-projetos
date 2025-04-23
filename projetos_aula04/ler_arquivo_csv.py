import csv

caminho_do_arquivo: str = "C:/Users/Rafasansou/Documents/bootcamp_intensivo_python/projetos_aula04/dataset.csv"

arquivo_csv: list = []

with open(file=caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)
    
print(arquivo_csv)