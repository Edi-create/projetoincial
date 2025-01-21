# CONSTANTE PYTHON é escrito em maiusculo por causa da convenção
CONSTANTE_BONUS = 1000.00

# 1) Solicita ao usuário que digite seu nome
nome = str(input("Qual o seu nome? "))
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Informe o seu salário: R$"))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Informe o valor do bônus recebido: "))
# 4) Calcule o valor do bônus final
bonus_recebido = CONSTANTE_BONUS + salario * bonus
# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá{nome}, o seu bônus foi de R${bonus_recebido}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?