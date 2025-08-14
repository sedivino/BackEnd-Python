# Exercício01:Faça um algoritmo que leia dois números inteiros positivos
# e mostre ao final qual deles é o menor. Caso os números sejam iguais
# mostre uma mensagem para o usuário informando isso.

# Início do programa
def recebeNumero():
    # Loop para receber e validar o número digitado pelo usuário
    while True:
        try:
            numero = int(input("Digite um número inteiro e positivo: "))
            if numero > 0:
                return numero
            else:
                print("O numero deve ser positivo. Digite novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def comparaNumeros(num1, num2):
    if num1 < num2:
        mensagem = print(f"O menor número é: {num1}")
        return mensagem
    elif num2 < num1:
        mensagem = print(f"O menor número é: {num2}")
        return mensagem
    else:
        mensagem = f"Os números são iguais."
        return mensagem

def main():
    print("===== Programa que compara dois números =====")
    
    num1 = recebeNumero()
    num2 = recebeNumero()

    resultado = comparaNumeros(num1, num2)
    print(resultado)

if __name__ == "__main__":
    main()

# Fim do programa
