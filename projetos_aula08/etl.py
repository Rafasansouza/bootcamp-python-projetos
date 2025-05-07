import pandas as pd
import os
import glob

# uma funcao de extract que le e consolida os json

def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_concatenado = pd.concat(df_list, ignore_index=True)
    return df_concatenado 

# uma funcao que transforma

def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# uma funcao que da load em csv ou parquet

def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro que vai ser "csv" ou "parquet" ou ambos
    """
    for saida in format_saida:
        if saida == 'csv':
            df.to_csv("dados.csv", index=False)
        if saida == 'parquet':
            df.to_parquet("dados.parquet", index=False)

# Pipeline

def calcular_kpi_extrair_arquivos_consolidado(pasta, formato_de_saida: list):
    dataframe = extrair_dados_e_consolidar(path=pasta)
    dataframe_kpi = calcular_kpi_de_total_de_vendas(dataframe)
    carregar_dados(dataframe_kpi, formato_de_saida)