# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

nome = input("Digite seu nome em minusculo: ").upper()
print(f"Seu nome em maiusculo é: {nome}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome = input("Digite seu nome em maiusculo: ").lower()
print(f"Seu nome em maiusculo é: {nome}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.


frase = input("Digite uma frase: ").strip()
print(frase)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input("Digite uma data no formato dd/mm/aaaa: ").split(sep= "/")
print(data)


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite todo o seu sobrenome: ")
nome_completo = primeiro_nome + " " + sobrenome
print("Seu nome completo é: ", nome_completo)