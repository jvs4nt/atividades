# O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor
# e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28%
# e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever
# o custo final ao consumidor.

print(" ")

somaImpostos = 0
somaDist = 0
custo = 0
total = 0

custo = float(input("digite o valor do seu carro: "))

somaDist = (custo * 28)/100

print(f"o valor da taxa do distribuidor será de {somaDist}")

somaImpostos = (custo * 45)/100

print(f"o valor dos impostos será de {somaImpostos}")

total = custo + somaImpostos + somaDist

print(f"o valor total do seu carro + taxas será de {total}")

print(" ")