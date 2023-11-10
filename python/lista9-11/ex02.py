def valorPagamento(valor_prestacao, dias_atraso):

    if dias_atraso == 0:
        # Sem atraso, cobrar apenas o valor da prestação
        valor_a_pagar = valor_prestacao
    else:
        # Com atraso, calcular multa e juros
        multa = 0.03 * valor_prestacao  # 3% de multa
        juros = 0.001 * dias_atraso * valor_prestacao  # 0,1% de juros por dia de atraso
        valor_a_pagar = valor_prestacao + multa + juros
    
    return valor_a_pagar

# Solicita ao usuário o valor da prestação e o número de dias em atraso
valor_prestacao = float(input("Digite o valor da prestação: "))
dias_atraso = int(input("Digite o número de dias em atraso: "))

# Chama a função valorPagamento e exibe o resultado
resultado = valorPagamento(valor_prestacao, dias_atraso)
print(f'O valor a ser pago é: {resultado}')