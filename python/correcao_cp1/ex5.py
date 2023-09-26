n1 = float(input("digite o primeiro valor: "))
n2 = float(input("digite o segundo valor: "))

print("1 - soma")
print("2 - subtracao")
print("3 - multiplicacao")
print("4 - divisao")

op = int(input("digite a opcao desejada: "))

match op:
    case 1:
        soma = n1 + n2
        print(f"resultado: {soma:.2f}")
    case 2:
        sub = n1 - n2
        print(f"resultado: {sub:.2f}")
    case 3:
        mult = n1 * n2
        print(f"resultado: {mult:.2f}")
    case 4:
        div = n1 / n2
        print(f"resultado: {div:.2f}")
    case _:
        print("opcao invalida")