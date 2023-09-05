num_x = float(input("digite um numero real: "))

opcao = int(input("digite uma opcao de 1 a 3: "))

match opcao:
    case 1:
        num_x = num_x + 5
    case 2:
        num_x = num_x - 4
    case 3: 
        num_x = num_x * 2
    case _:
        print("opcao invalida")

print(f"valor da variavel X é: {num_x:.2f}")