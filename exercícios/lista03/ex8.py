'''
Tendo como dados de entrada a altura e o sexo de uma pessoa
(M ou F), construa um algoritmo que calcule seu peso ideal
usando as seguintes fórmulas:
- para homens: (72.7 * h) - 58
- para mulheres: (62.1 * h) - 44.7
'''

# Início do programa
def recebe_altura(mensagem, minimo=0):
    # Recebe e valida uma altura positiva do usuário
    while True:
        try:
            valor = float(input(mensagem))
            if valor >= minimo:
                return valor
            else:
                print(f"O valor deve ser maior ou igual a {minimo}. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido.")

def recebe_sexo(mensagem):
    while True:
        sexo = input(mensagem).strip().upper()
        if sexo in ['M', 'F']:
            return sexo
        else:
            print("Entrada inválida. Digite 'M' para masculino ou 'F' para feminino.")

def calcula_peso_ideal(altura, sexo):
    if sexo == 'M':
        return (72.7 * altura) - 58
    else:  # sexo == 'F'
        return (62.1 * altura) - 44.7
    
def main():
    print("===== Cálculo do Peso Ideal =====")
    altura = recebe_altura("Digite a altura (em metros): ", minimo=0.5)
    sexo = recebe_sexo("Digite o sexo (M/F): ")

    peso_ideal = calcula_peso_ideal(altura, sexo)
    print(f"O peso ideal para uma pessoa com altura {altura:.2f}m e sexo '{sexo}' é: {peso_ideal:.2f} kg")

if __name__ == "__main__":
    main()

# Fim do programa