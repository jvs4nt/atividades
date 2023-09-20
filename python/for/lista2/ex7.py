# Desenvolva um programa que receba um número inteiro positivo n. Exiba na tela a tabuada de multiplicação (0 ao 10) para o número informado pelo usuário.

n = int(input("Digite um número inteiro positivo: "))

if n < 0:
    print("O número deve ser positivo.")
else:
    print(f"Tabuada de multiplicação para {n}:")
    for i in range(11):
        r = n * i
        print(f"{n} x {i} = {r}")
