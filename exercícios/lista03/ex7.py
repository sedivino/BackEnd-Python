'''Escreva um algoritmo que lê o número de um vendedor de uma empresa, seu salário fixo e o total de vendas
por ele efetuadas. Sabe-se que cada vendedor recebe um salário fixo, mais uma comissão proporcional às vendas
por ele efetuadas. A comissão é de 3% sobre o total das vendas até R$ 10 mil e 5% sobre o que ultrapassa
este valor. Escreva o número do vendedor, o total de suas vendas, seu salário fixo e o total a receber'''

# Início do programa
def recebeNumeroVendedor():
    while True:
        try:
            numero = int(input("Digite o número do vendedor: "))
            if numero > 0:
                return numero
            else:
                print("O número do vendedor deve ser positivo. Digite novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def recebeSalarioFixo():
    while True:
        try:
            salario = float(input("Digite o salário fixo do vendedor: "))
            if salario >= 0:
                return salario
            else:
                print("O salário deve ser um valor não negativo. Digite novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido.")

def recebeTotalVendas():
    while True:
        try:
            vendas = float(input("Digite o total de vendas efetuadas pelo vendedor: "))
            if vendas >= 0:
                return vendas
            else:
                print("O total de vendas deve ser um valor não negativo. Digite novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido.")

def calculaComissao(vendas):
    if vendas <= 10000:
        return vendas * 0.03
    else:
        return 10000 * 0.03 + (vendas - 10000) * 0.05

def main():
    print("===== Programa de Comissão de Vendedores =====")

    numero_vendedor = recebeNumeroVendedor()
    salario_fixo = recebeSalarioFixo()
    total_vendas = recebeTotalVendas()

    comissao = calculaComissao(total_vendas)
    total_a_receber = salario_fixo + comissao

    print(f"\nNúmero do Vendedor: {numero_vendedor}")
    print(f"Salário Fixo: R$ {salario_fixo:.2f}")
    print(f"Total de Vendas: R$ {total_vendas:.2f}")
    print(f"Total a Receber: R$ {total_a_receber:.2f}")

if __name__ == "__main__":
    main()

# Fim do programa   