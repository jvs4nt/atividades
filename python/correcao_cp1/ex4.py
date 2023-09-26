qtd_morango = int(input("digite a quantidade de morangos(kg): "))
qtd_maca = int(input("digite a quantidade de maças(kg): "))

total_kg = qtd_morango + qtd_maca

if (qtd_morango <= 5):
    valor_morango = qtd_morango * 2.50
else:
    valor_morango = qtd_morango * 2.20

if (qtd_maca <= 5):
    valor_maca = qtd_maca * 1.80
else:
    valor_maca = qtd_maca * 1.50

valor_total = valor_maca + valor_morango

if (total_kg > 8) or (valor_total > 25.00):
    valor_total = valor_total * 0.90

print(f"valor: R${valor_total}")