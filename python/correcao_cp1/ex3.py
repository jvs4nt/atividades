saque = float(input("digite o valor a sacar: "))

if (saque % 10 == 0):
    ced50 = saque // 50
    quantia = saque % 50

    ced20 = quantia // 20
    quantia = quantia % 20

    ced10 = quantia // 10

    print(f"celulas de 50: {ced50:.0f}")
    print(f"celulas de 20: {ced20:.0f}")
    print(f"celulas de 10: {ced10:.0f}")

else:
    print("valor invalido! por favor digite um numero multiplo de 10")