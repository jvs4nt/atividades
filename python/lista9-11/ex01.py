def soma(taxa, custo):
    imposto = custo * (taxa / 100)
    custo_imposto = custo + imposto

    return custo_imposto

taxaImposto = 10
custoItem = 100

novoCusto = soma(taxaImposto, custoItem)
print(f"Novo custo: {novoCusto}")