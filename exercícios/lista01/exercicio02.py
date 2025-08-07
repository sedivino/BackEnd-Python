''' Crie um código que receba o salário de um vendedor, o total de vendas e a porcentagem de comissão.
 O programa deve calcular o salário total do vendedor, que é a soma do salário base com a comissão.
 A comissão é calculada como o total de vendas multiplicado pela porcentagem de comissão.
'''

def ler_salario_base():
    while True:
        try:
            salario = float(input("Digite o salário base do vendedor: R$ "))
            if salario < 0:
                print("Salário não pode ser negativo. Tente novamente.")
            else:
                return salario
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def ler_total_vendas():
    while True:
        try:
            total_vendas = float(input("Digite o total de vendas do vendedor: R$ "))
            if total_vendas < 0:
                print("Total de vendas não pode ser negativo. Tente novamente.")
            else:
                return total_vendas
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def ler_porcentagem_comissao():
    while True:
        try:
            porcentagem = float(input("Digite a porcentagem de comissão (em %): "))
            if porcentagem < 0 or porcentagem > 100:
                print("Porcentagem inválida. Deve ser entre 0 e 100. Tente novamente.")
            else:
                return porcentagem / 100  # Convertendo para decimal
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def calcular_salario_total(salario_base, total_vendas, porcentagem_comissao):
    comissao = total_vendas * porcentagem_comissao
    return salario_base + comissao

def main():
    print("Calculadora de Salário do Vendedor")
    
    # Ler dados do vendedor
    salario_base = ler_salario_base()
    total_vendas = ler_total_vendas()
    porcentagem_comissao = ler_porcentagem_comissao()

    # Calcular salário total
    salario_total = calcular_salario_total(salario_base, total_vendas, porcentagem_comissao)
    
    print(f"Salário total do vendedor: R$ {salario_total:.2f}")

if __name__ == "__main__":
    main()

# Fim do programa
