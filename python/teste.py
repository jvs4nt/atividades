#importa a biblioteca que permite limpar a tela
import os

#cria uma função clear() para chamar sempre que quiser limpar
#assim, nao precisa repetir "os.system("clear") or None" toda vez
def clear():
    os.system("clear") or None

clear() #ja inicia o codigo com a tela limpa

n1 = int(input("digite um numero inteiro: "))

n2 = int(input("digite outro numero inteiro: "))

soma = n1 + n2

clear() #limpa novamente para mostrar o resultado isolado

print(f"a soma dos numeros é: {soma}")