# Calculando a média de três notas
# e verificando se o aluno foi aprovado ou reprovado

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aluno aprovado com média {media:.2f}")
else:
    print(f"Aluno reprovado com média {media:.2f}")
# Fim do programa
