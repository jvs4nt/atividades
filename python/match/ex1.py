codigo = input("Digite o código do produto: ")


match codigo:
    case "01":
        descricao = "Caneta"
        preco = 1.20
    case "02":
        descricao = "Lápis"
        preco = 0.80
    case "03":
        descricao = "Caderno"
        preco = 4.50
    case "04":
        descricao = "Borracha"
        preco = 1.00
    case "05":
        descricao = "Régua"
        preco = 1.50
    case _:
        descricao = "Produto não cadastrado"
        preco = 0.00 

print(f"Descrição: {descricao}")
print(f"Preço: R${preco:.2f}")
