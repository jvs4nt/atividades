total = 0

preco = float(input("digite o preco da mercadoria: "))

while (preco != 0):
    qtd = int(input("digite a quantidade da mercadoria: "))

    total = total + (qtd * preco)
    preco = float(input("digite o preco da mercadoria: "))

print(f"valor total: {total:.2f}")