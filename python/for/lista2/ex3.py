# Desenvolva um programa para calcular a média salarial dos funcionários da empresa XXX,
# para isso seu programa deverá solicitar o nome e salário dos 5 funcionários que trabalham
# nessa empresa. Ao final seu programa deverá calcular a média dos salários e exibir na
# tela as seguintes informações: (use 2 casas decimais na exibição dos números)

#a A média salarial dos funcionários da empresa XXX é _______

#o O nome e o salário do funcionário que recebe o menor salário

#o O nome e o salário do funcionário que recebe o maior salário

min_sal = float('inf')
max_sal = float('-inf')
n_min = ""
n_max = ""

soma = 0

for i in range(5):
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    soma += salario

    if salario < min_sal:
        min_sal = salario
        n_min = nome

    if salario > max_sal:
        max_sal = salario
        n_max = nome

media = soma / 5

print(f"A média salarial dos funcionários da empresa XXX é {media:.2f}")
print(f"O nome e o salário do funcionário que recebe o menor salário são: {n_min} - {min_sal:.2f}")
print(f"O nome e o salário do funcionário que recebe o maior salário são: {n_max} - {max_sal:.2f}")