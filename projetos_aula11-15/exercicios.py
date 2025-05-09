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

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação