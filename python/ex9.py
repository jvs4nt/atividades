peso = float(input("digite o seu peso (ex. 77): "))
altura = float(input("digite sua altura (ex. 1.75): "))

imc = peso / (altura**2)

if imc <= 18.5:
    print(f"o imc é {imc:.2f}, voce esta abaixo do peso")
elif (imc > 18.5 and imc <= 24.9):
    print(f"o imc é {imc:.2f}, voce esta no peso ideal")
else:
    print(f"o imc é {imc:.2f}, voce esta acima do peso")