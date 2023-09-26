salario_fixo = float(input("digite o salario fixo do funcionario: "))
comissao_fixa = float(input("digite o valor da comissao por carro vendido: "))
n_carros = int(input("digite o numero de carros vendidos: "))
valor_vendas = float(input("digite o valor total das vendas: "))

salario_final = salario_fixo + (n_carros * comissao_fixa) + (valor_vendas * 0.05)

print(f"salario final: R${salario_final}")