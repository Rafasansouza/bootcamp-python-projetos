# Implementação do algoritmo de ordenação por seleção
lista = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Ordenando a lista
print("Lista ordenada com função personalizada:", lista)

# Lista de exemplo
lista2 = [64, 34, 25, 12, 22, 11, 90]

# Ordenando a lista com sort()
lista2.sort()

print("Lista ordenada com método built-in:", lista2)

# Exemplo: Transformação de Dados com Funções

def normalizar_nome(nome: str) -> str:
    return nome.strip().lower()

nomes = [" Alice ", "BOB", "Carlos"]
nomes_normalizados = [normalizar_nome(nome) for nome in nomes]
print(nomes_normalizados)

#Tipagem dos Parâmetros

def saudacao(nome: str, idade: int) -> str:
    return f"Olá, {nome}, você tem {idade} anos."

#Parâmetros com Valores Default

def saudacao(nome: str, idade: int = 30) -> str:
    return f"Olá, {nome}, você tem {idade} anos."

