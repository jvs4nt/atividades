num_horas = int(input("digite o numero de horas trabalhadas no mes: "))
salario_hora = float(input("digite o valor do salario por hora: "))

if (num_horas >= 160):
    salario_mes = (salario_hora * 160) + (num_horas - 160) * (salario_hora * 1.50)
else:
    salario_mes = num_horas * salario_hora

print(f"salario do funcionario: R${salario_mes:.2f}")