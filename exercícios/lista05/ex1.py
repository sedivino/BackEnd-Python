# Criando os vetores
vetor1 = []
vetor2 = []
vetor_soma = []

# Lendo os valores dos vetores
for i in range(5):
    num1 = int(input(f"Digite o {i+1}º número do primeiro vetor: "))
    vetor1.append(num1)

for i in range(5):
    num2 = int(input(f"Digite o {i+1}º número do segundo vetor: "))
    vetor2.append(num2)

# Somando os vetores
for i in range(5):
    soma = vetor1[i] + vetor2[i]
    vetor_soma.append(soma)

# Mostrando o vetor resultante
print("Vetor resultante da soma:")
print(vetor_soma)

# Fim do código