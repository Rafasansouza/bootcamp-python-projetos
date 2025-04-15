# Instruções do desafio:
# O programa deve começar solicitando ao usuário que insira seu nome.
# Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
# Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
# O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
# Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

name_user = input("Digite seu nome: ")

salary_user = float(input("Digite seu salario(format: #####.##): "))

percent_bonus = float(input("Digite o percentual do bônus (0 a 100): "))/100 + 1

calc_kpi = 1000 + salary_user * percent_bonus

print(f"Olá {name_user}, o seu valor bônus foi de R$ {calc_kpi}")