# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

num_1 = float(input("Digite o primeiro número decimal: "))
num_2 = float(input("Digite o segundo número decimal: "))
soma = num_1 + num_2
print("A soma é:", soma)

# # 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num_1 = float(input("Digite o primeiro número decimal: "))
num_2 = float(input("Digite o segundo número decimal: "))
media = (num_1 + num_2) / 2
print("A soma é:", media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input("Digite a base em número decimal: "))
exp = float(input("Digite o expoente em número decimal: "))
potenc = base ** exp
print("A soma é:", potenc)


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

temp_C = float(input("Digite a temperatura em °C: "))
convert_to_F = (temp_C * (9/5)) + 32
print(f"{temp_C} °C equivalem {convert_to_F} °F.")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math
raio_circulo = float(input("Digite o raio do circulo em cm: "))
area_circulo = math.pi * (raio_circulo ** 2)
# area_do_circulo_formatada = "{:.2f}".format{area_circulo}
print(f"A area do circulo equivale {area_circulo:.2f} cm².")