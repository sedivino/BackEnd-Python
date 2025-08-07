'''
O programa deve receber o salário de uma pessoa e calcular o quanto sobrará após pagar duas contas que
estão atrasadas. As contas são informadas pelo usuário e terão um acréscimo de 2% sobre o valor original.
O programa deve tratar a entrada para garantir que o usuário digite um número válido para o salário e os valores das contas
'''

# Início do programa
def ler_salario():
    while True:
        try:
            salario = float(input("Digite o salário da pessoa: R$ "))
            if salario < 0:
                print("Salário não pode ser negativo. Tente novamente.")
            else:
                return salario
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def ler_conta(nome_conta):
    while True:
        try:
            conta = float(input(f"Digite o valor da {nome_conta} (R$): "))
            if conta < 0:
                print(f"Valor da {nome_conta} não pode ser negativo. Tente novamente.")
            else:
                return conta
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def calcular_valor_final(conta):
    return conta * 1.02  # Acrescenta 2% ao valor da conta

def calcular_saldo_final(salario, conta1, conta2):
    valor_final_conta1 = calcular_valor_final(conta1)
    valor_final_conta2 = calcular_valor_final(conta2)
    return salario - (valor_final_conta1 + valor_final_conta2)

def main():
    print("Calculadora de Saldo Após Pagamento de Contas")
    print(f"====================================")
    
    # Ler salário e contas
    salario = ler_salario()
    conta1 = ler_conta("primeira conta")
    conta2 = ler_conta("segunda conta")

    # Calcular saldo final
    saldo_final = calcular_saldo_final(salario, conta1, conta2)
    
    if saldo_final < 0:
        print(f"Saldo insuficiente após o pagamento das contas. Saldo final: R$ {saldo_final:.2f}")
    else:
        print(f"Saldo final após o pagamento das contas: R$ {saldo_final:.2f}")

if __name__ == "__main__":
    main()

# Fim do programa
