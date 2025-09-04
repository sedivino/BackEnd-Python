# Faça um programa que leia dois vetores de dez elementos inteiros cada um e mostre um vetor
# resultante da intercalação desses dois vetores.

# Criando os vetores e o vetor resultante:
vetor1 = []
vetor2 = []
vetor_resultante = []

# Lendo os valores dos vetores:
for i in range(10):
    num1 = int(input(f"Digite o {i+1}º número do primeiro vetor: "))
    vetor1.append(num1)


for i in range(10):
    num2 = int(input(f"Digite o {i+1}º número do segundo vetor: "))
    vetor2.append(num2)

    vetor_resultante.append(num2)

# Intercalando os vetores:
for i in range(10):
    vetor_resultante.insert(2*i, vetor1[i])

# Mostrando o vetor resultante:
print("Vetor resultante da intercalação:")
print(vetor_resultante)

# Fim do código