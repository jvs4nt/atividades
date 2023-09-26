# Escreva um algoritmo que solicite dois números e devolva quantos pares e ímpares há entre esses dois números.
#  Exemplo: entre 7 e 10 há 2 números pares e 2 números ímpares

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

p = 0
i = 0

for numero in range(n1, n2 + 1):
    if numero % 2 == 0:
        p += 1
    else:
        i += 1

print(f"Entre {n1} e {n2} há {p} números pares e {i} números ímpares.")