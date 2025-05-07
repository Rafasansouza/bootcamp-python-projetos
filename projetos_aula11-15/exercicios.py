import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 + numero_02
print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero_01 = int(input("Inserir um numero inteiro: "))
resultado = numero_01 % 5
print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 * numero_02
print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero_01 = int(input("Inserir um numero inteiro: "))
resultado = numero_01 ** 2
print(resultado)
