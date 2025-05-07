from etl import calcular_kpi_extrair_arquivos_consolidado

pasta: str = 'data'
formato_de_saida: list = ["csv", "parquet"]

calcular_kpi_extrair_arquivos_consolidado(pasta, formato_de_saida)