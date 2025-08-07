# Calculando a média de três notas e verificando se o aluno foi aprovado ou reprovado.
# A média para aprovação é 7.0.
# O programa deve verificar se a nota digitada é válida (entre 0 e 10) e tratar o erro caso a entrada não seja um número.

# Inicio do programa
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def verificar_aprovacao(media):
    """Verifica se a média é suficiente para aprovação."""
    if media < 0:
        raise ValueError("A média não pode ser negativa.")
    elif media > 10:
        raise ValueError("A média não pode ser maior que 10.")
    return media >= 7.0

def obter_nota_valida(numero_nota):
    while True:
        try:
            nota = float(input(f"Digite a nota {numero_nota} (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


def main():
    print("Calculadora de Média de Notas")
    
    # Obter notas válidas do usuário
    nota1 = obter_nota_valida(1)
    nota2 = obter_nota_valida(2)
    nota3 = obter_nota_valida(3)

    # Calcular a média
    media = calcular_media(nota1, nota2, nota3)
    
    # Verificar se o aluno foi aprovado ou reprovado
    try:
        if verificar_aprovacao(media):
            print(f"Aluno aprovado com média: {media:.2f}")
        else:
            print(f"Aluno reprovado com média: {media:.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# Fim do programa