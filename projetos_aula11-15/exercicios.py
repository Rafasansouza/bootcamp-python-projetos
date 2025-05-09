import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero_01: int = int(input("Inserir um numero inteiro: "))
numero_02: int = int(input("Inserir outro numero inteiro: "))
resultado: int = numero_01 + numero_02
print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero_01: int = int(input("Inserir um numero inteiro: "))
resultado: int = numero_01 % 5
print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero_01: int = int(input("Inserir um numero inteiro: "))
numero_02: int = int(input("Inserir outro numero inteiro: "))
resultado: int = numero_01 * numero_02
print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero_01: int = int(input("Inserir um numero inteiro: "))
numero_02: int = int(input("Inserir outro numero inteiro: "))
resultado: int = numero_01 // numero_02
print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero_01: int = int(input("Inserir um numero inteiro: "))
resultado: int = numero_01 ** 2
print(resultado)

# #### Números de Ponto Flutuante (`float`)

import math

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

numero_01: float = float(input("Inserir um numero float: "))
numero_02: float = float(input("Inserir outro numero float: "))
resultado: float = numero_01 + numero_02
print(resultado)

# Exercício 7 - Média de dois números flutuantes
try:
    numero1: float = float(input("Digite o primeiro número (float): "))
    numero2: float = float(input("Digite o segundo número (float): "))
    media: float = (numero1 + numero2) / 2
    print(f"A média entre {numero1} e {numero2} é: {media:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")

# Exercício 8 - Potência de um número
try:
    base: float = float(input("\nDigite a base da potência: "))
    expoente: float = float(input("Digite o expoente: "))
    potencia: float = base ** expoente
    print(f"{base} elevado a {expoente} é: {potencia}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")

# Exercício 9 - Conversão Celsius para Fahrenheit
try:
    celsius: float = float(input("\nDigite a temperatura em Celsius: "))
    fahrenheit: float = (celsius * 9 / 5) + 32
    print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")
except ValueError:
    print("Por favor, insira um valor numérico para a temperatura.")

# Exercício 10 - Cálculo da área de um círculo
try:
    raio: float = float(input("\nDigite o raio do círculo: "))
    area: float = math.pi * raio ** 2
    print(f"A área do círculo com raio {raio} é: {area:.2f}")
except ValueError:
    print("Por favor, insira um valor numérico para o raio.")

# #### Strings (`str`)

# Exercício 11 - Converter string para maiúsculas
entrada_maiuscula: str = input("Digite uma palavra ou frase para converter em maiúsculas: ")
resultado_maiuscula: str = entrada_maiuscula.upper()
print(f"Resultado em maiúsculas: {resultado_maiuscula}")

# Exercício 12 - Converter nome completo para minúsculas
nome_completo: str = input("\nDigite seu nome completo: ")
nome_minusculo: str = nome_completo.lower()
print(f"Nome em minúsculas: {nome_minusculo}")

# Exercício 13 - Remover espaços em branco do início e fim da frase
frase_com_espacos: str = input("\nDigite uma frase com espaços no início e/ou fim: ")
frase_sem_espacos: str = frase_com_espacos.strip()
print(f"Frase sem espaços nas extremidades: '{frase_sem_espacos}'")

# Exercício 14 - Separar data no formato dd/mm/aaaa
data: str = input("\nDigite uma data no formato dd/mm/aaaa: ")
partes_data: list[str] = data.split("/")
if len(partes_data) == 3:
    dia: str = partes_data[0]
    mes: str = partes_data[1]
    ano: str = partes_data[2]
    print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")
else:
    print("Formato de data inválido. Use dd/mm/aaaa.")

# Exercício 15 - Concatenar duas strings
string1: str = input("\nDigite a primeira string: ")
string2: str = input("Digite a segunda string: ")
concatenada: str = string1 + string2
print(f"Resultado da concatenação: {concatenada}")

# #### Booleanos (`bool`)

# Exercício 16 - Operação AND entre duas expressões booleanas
entrada_1: str = input("Digite a primeira expressão booleana (True ou False): ")
entrada_2: str = input("Digite a segunda expressão booleana (True ou False): ")
bool_1: bool = entrada_1.strip().capitalize() == "True"
bool_2: bool = entrada_2.strip().capitalize() == "True"
resultado_and: bool = bool_1 and bool_2
print(f"Resultado da operação AND: {resultado_and}")

# Exercício 17 - Operação OR entre dois valores booleanos
entrada_3: str = input("\nDigite o primeiro valor booleano (True ou False): ")
entrada_4: str = input("Digite o segundo valor booleano (True ou False): ")
bool_3: bool = entrada_3.strip().capitalize() == "True"
bool_4: bool = entrada_4.strip().capitalize() == "True"
resultado_or: bool = bool_3 or bool_4
print(f"Resultado da operação OR: {resultado_or}")

# Exercício 18 - Inverter um valor booleano
entrada_5: str = input("\nDigite um valor booleano (True ou False): ")
bool_5: bool = entrada_5.strip().capitalize() == "True"
bool_invertido: bool = not bool_5
print(f"Valor invertido: {bool_invertido}")

# Exercício 19 - Comparar se dois números são iguais
numero_1: float = float(input("\nDigite o primeiro número: "))
numero_2: float = float(input("Digite o segundo número: "))
sao_iguais: bool = numero_1 == numero_2
print(f"Os números são iguais? {sao_iguais}")

# Exercício 20 - Verificar se dois números são diferentes
numero_3: float = float(input("\nDigite o primeiro número: "))
numero_4: float = float(input("Digite o segundo número: "))
sao_diferentes: bool = numero_3 != numero_4
print(f"Os números são diferentes? {sao_diferentes}")

# #### try-except e if

# Exercício 21 - Conversor de Temperatura (Celsius para Fahrenheit)
try:
    temperatura_celsius: float = float(input("Digite a temperatura em Celsius: "))
    temperatura_fahrenheit: float = (temperatura_celsius * 9/5) + 32
    print(f"Temperatura em Fahrenheit: {temperatura_fahrenheit:.2f}°F")
except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")

# Exercício 22 - Verificador de Palíndromo
palavra: str = input("\nDigite uma palavra para verificar se é um palíndromo: ").strip()
palavra_invertida: str = palavra[::-1]
if palavra.lower() == palavra_invertida.lower():
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")

# Exercício 23 - Calculadora Simples
try:
    numero_1: float = float(input("\nDigite o primeiro número: "))
    operador: str = input("Digite o operador (+, -, *, /): ").strip()
    numero_2: float = float(input("Digite o segundo número: "))

    resultado: float
    if operador == "+":
        resultado = numero_1 + numero_2
    elif operador == "-":
        resultado = numero_1 - numero_2
    elif operador == "*":
        resultado = numero_1 * numero_2
    elif operador == "/":
        if numero_2 != 0:
            resultado = numero_1 / numero_2
        else:
            print("Erro: divisão por zero.")
            resultado = None
    else:
        print("Operador inválido.")
        resultado = None

    if resultado is not None:
        print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: insira apenas números válidos.")

# Exercício 24 - Classificador de Números
try:
    numero: float = float(input("\nDigite um número para classificar: "))
    if numero > 0:
        print("Número positivo.")
    elif numero < 0:
        print("Número negativo.")
    else:
        print("Número zero.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número.")

# Exercício 25 - Conversão de Tipo com Validação
entrada: str = input("\nDigite um número inteiro: ")
try:
    numero_inteiro: int = int(entrada)
    print(f"Número convertido com sucesso: {numero_inteiro}")
except ValueError:
    print("Erro: valor digitado não é um número inteiro válido.")