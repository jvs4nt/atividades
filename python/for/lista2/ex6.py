# Escreva um programa que calcule o somatório de todos os números pares em um intervalo definido pelo usuário.
# Ex: para inicio = 2 e fim = 10 o somatório é 2+4+6+8+10. OBS: utilize o “for”.

i = int(input("Digite o valor de início do intervalo: "))
f = int(input("Digite o valor de fim do intervalo: "))

s = 0

for num in range(i, f + 1):
    if num % 2 == 0:
        s += num

print(f"O somatório dos números pares no intervalo de {i} a {f} é {s}")
