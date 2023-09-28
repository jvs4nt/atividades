res = "s"

while (res != "n"):
    print("1 - verificar se o X é divisível por 6")
    print ("2 - cacular o fatorial do numero")
    print ("3 - exibir todos os inteiros de 1 ate o X")

    x = int(input("digite o valor de x: "))
    opc = int(input("digite a opcao desejada: "))

    match opc:
        case 1:
            if(x % 6 == 0):
                print ("o numero é divisivel por 6")
            else:
                print("o numero nao é divisivel por 6")

        case 2:
            fat = 1
            for i in range(1, x+1):
                fat = fat * 1
                print(f"o fatorial de {i} é {fat}")

        case 3:
            for i in range(1, x+1):
                print (i)

        case _:
            print("opcao invalida")

res = input("deseja continuar? (s - sim / n - nao)")