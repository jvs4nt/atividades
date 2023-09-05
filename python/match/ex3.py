n1 = float(input("digite o numero 1: "))

n2 = float(input("digite o numero 2: "))

opcao = int(input("digite uma opcao de 1 a 4"))

match opcao:
    case 1:
        soma = n1 + n2
        print(f"o valor da soma é {soma:.2f}")
    case 2:
        sub = n1 - n2
        print(f"o valor da subtracao é {sub:.2f}")
    case 3:
        mult = n1 * n2
        print(f"a multiplicacao é: {mult:.2f}")
    case 4:
        div = n1 / n2
        print(f"o valor da divisao é: {div:.2f}")