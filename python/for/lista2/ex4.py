# Desenvolva um programa que receba:

# o taxa de abatimento em porcentagem;

# o número de prestações;

# o valor da primeira prestação.

# Seu programa deverá exibir na tela os valores das prestações decrescente dado que
# a cada mês o valor da prestação diminui do valor da prestação do mês anterior 
# (utilize a taxa de abatimento fornecida pelo usuário para realizar esse cálculo). OBS: utilize o “for”.

t = float(input("Digite a taxa de abatimento em porcentagem: "))
n = int(input("Digite o número de prestações: "))
p = float(input("Digite o valor da primeira prestação: "))

t = t / 100
pa = p

for _ in range(n):
    print(f"Prestação: R$ {pa:.2f}")
    pa = pa - (pa * t)

print(f"Valor da última prestação: R$ {pa:.2f}")