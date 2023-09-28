soma = 0
qtd = 0

n1 = int(input("digite um numero: "))

while (n1 != 0):
    if (n1 > 0):
        soma += n1
        qtd += 1
        if (qtd == 1):
            maior = n1
            menor = n1
        else:
            if (n1 > maior):
                maior = n1
            if (n1 < menor):
                menor = n1

    n1 = int(input("digite um numero: "))

media = soma / qtd

print(f"media: {media:.2f}")
print(f"maior numero: {maior:.2f}")
print(f"menor numero: {menor:.2f}")