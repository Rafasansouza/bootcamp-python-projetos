### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

try:
    name_user = str(input("Digite seu nome: "))
    salary_user = float(input("Digite seu salario(format: #####.##): "))
    bonus = float(input("Digite o percentual do bônus (0 a 100): "))

    if bonus >= 0 and bonus <= 100:
        percent_bonus = bonus/100 + 1
        calc_kpi = 1000 + salary_user * percent_bonus
        print(f"Olá {name_user}, o seu valor bônus foi de R$ {calc_kpi}")
    else:
        print("Você digitou o bonus no formato incorreto ou fora do range!")
except ValueError:
    print("Erro: Há variaveis que não segue o requisito solicitado. Revise!")