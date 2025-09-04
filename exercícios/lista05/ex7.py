# Faça um programa que leia dois vetores de dez elementos inteiros cada um e mostre um vetor
# resultante da intercalação desses dois vetores.

'''
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
'''
# Criando os vetores e o vetor resultante:
vetor1 = [3, 5, 4, 2, 2, 5, 3, 2, 5, 9]
vetor2 = [3, 5, 4, 2, 2, 5, 3, 2, 5, 9]
vetor_resultante = []

# Intercalando os vetores:
for i in range(10):
    vetor_resultante.append(vetor1[i])
    vetor_resultante.append(vetor2[i])

# Mostrando o vetor resultante:
print("Vetor resultante da intercalação:")
print(vetor_resultante)

# Fim do código