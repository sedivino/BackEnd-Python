# Exercício01:Faça um algoritmo que leia dois números inteiros positivos
# e mostre ao final qual deles é o menor. Caso os números sejam iguais
# mostre uma mensagem para o usuário informando isso.

# Início do programa
def recebeNumero():
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
        return f"O menor número é: {num1}"
    elif num2 < num1:
        return f"O menor número é: {num2}"
    else:
        return "Os números são iguais."

def main():
    print("===== Programa que compara dois números =====")
    
    num1 = recebeNumero()
    num2 = recebeNumero()
    
    if num1 < num2:
        print(f"O menor número é: {num1}")
    elif num2 < num1:
        print(f"O menor número é: {num2}")
    else:
        print("Os números são iguais.")

if __name__ == "__main__":
    main()
# Fim do programa
