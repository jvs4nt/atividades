tempo_perm = float(input("digite o tempo de permanencia no estabelecimento: "))

if (tempo_perm >= 7):
    print("o valor a pagar é de R$35")
else:
    valor_pagar = (tempo_perm * 5.00)
    print("o valor a pagar é de R${valor_pagar:.2f}")