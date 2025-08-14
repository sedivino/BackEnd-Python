'''Escreva um algoritmo que lê o número de um vendedor de uma empresa, seu salário fixo e o total de vendas
por ele efetuadas. Sabe-se que cada vendedor recebe um salário fixo, mais uma comissão proporcional às vendas
por ele efetuadas. A comissão é de 3% sobre o total das vendas até R$ 10 mil e 5% sobre o que ultrapassa
este valor. Escreva o número do vendedor, o total de suas vendas, seu salário fixo e o total a receber'''

# Início do programa
LIMITE_COMISSAO = 10000
TAXA1 = 0.03
TAXA2 = 0.05

def recebe_float_positivo(mensagem, minimo=0, inteiro=False):
    while True:
        try:
            entrada = input(mensagem)
            valor = int(entrada) if inteiro else float(entrada)
            if valor >= minimo:
                return valor
            else:
                print(f"O valor deve ser maior ou igual a {minimo}. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido.")

def calcula_comissao(vendas: float) -> float:
    if vendas <= LIMITE_COMISSAO:
        return vendas * TAXA1
    else:
        return LIMITE_COMISSAO * TAXA1 + (vendas - LIMITE_COMISSAO) * TAXA2

def exibir_relatorio(numero, salario, vendas, total):
    """Exibe o relatório do vendedor com os dados fornecidos."""
    print("\n" + "=" * 40)
    print("===== Relatório do Vendedor =====")
    print(f"Número do Vendedor : {numero}")
    print(f"Salário Fixo       : R$ {salario:.2f}")
    print(f"Total de Vendas    : R$ {vendas:.2f}")
    print(f"Total a Receber    : R$ {total:.2f}")

def main():
    print("===== Programa de Comissão de Vendedores =====")
    numero = recebe_float_positivo("Número do vendedor: ", minimo=1, inteiro=True)
    salario = recebe_float_positivo("Salário fixo: ")
    vendas = recebe_float_positivo("Total de vendas: ")

    comissao = calcula_comissao(vendas)
    total_receber = salario + comissao

    exibir_relatorio(numero, salario, vendas, total_receber)

if __name__ == "__main__":
    main()
# Fim do programa