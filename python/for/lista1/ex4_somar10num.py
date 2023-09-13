# Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40
# devem ser somados. Escreva o valor final da soma efetuada.

print(" ")

soma = 0

for i in range(1, 11):
    n = float(input(f"digite o numero {i}: "))

    if (n < 40):
        soma += n

print(f"a soma total dos numeros menores que 40 e: {soma}")

print(" ")