# Escreva um programa que faça a leitura das notas dos 3 checkpoints de 15 alunos e mostre a média dos 
# checkpoints para cada aluno.

print(" ")

for i in range(1, 16):
    soma = 0
    total = 0
    media = 0

    n1 = float(input(f"digite a primeira nota do aluno {i}: "))
    n2 = float(input(f"digite a segunda nota do aluno {i}: "))
    n3 = float(input(f"digite a terceira nota do aluno {i}: "))
    print(" ")

    soma = n1 + n2 + n3
    media = soma / 3

    print(f"a media do aluno {i} foi: {media}")
    print(" ")



