'''Faça um algoritmo que leia 3 valores a, b, c, quais quer e encontre o maior dos 3 escrevendo-o
com a mensagem: "É O MAIOR".'''

# Início do programa
def recebeNumero(numero):
    # Loop para receber e validar o número digitado pelo usuário
    while True:
        try:
            valor = float(input(f"Digite o {numero}º valor: "))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def encontraMaior(a, b, c):
    if a > b and a > c:
        return f"{a} É O MAIOR."
    elif b > a and b > c:
        return f"{b} É O MAIOR."
    else:
        return f"{c} É O MAIOR."

def main():
    print("===== Programa que encontra o maior de três números =====")

    a = recebeNumero(1)
    b = recebeNumero(2)
    c = recebeNumero(3)

    resultado = encontraMaior(a, b, c)
    print(resultado)

if __name__ == "__main__":
    main()

# Fim do programa