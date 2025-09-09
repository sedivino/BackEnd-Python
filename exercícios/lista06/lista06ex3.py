'''
Faça um algoritmo que carregue uma matriz 6 x 3, calcule e mostre:
• o maior elemento da matriz e sua respectiva posição, ou seja, linha e coluna;
• o menor elemento da matriz e sua respectiva posição, ou seja, linha e coluna.
'''
# Importando a biblioteca random para gerar números aleatórios
import random

# Inicializando a matriz e variáveis para maior e menor elementos
matriz = []
maior = menor = 0
pos_maior = pos_menor = (0, 0)

# Preenchendo a matriz com números aleatórios e encontrando maior e menor elementos
for i in range(6):
    # Criando uma nova linha
    linha = []
    # Adicionando 3 elementos à linha
    for j in range(3):
        # Gerando um número aleatório entre 0 e 100
        num = random.randint(0, 10)
        # Adicionando o número à linha
        linha.append(num)
        # Verificando se é o maior ou menor elemento
        if i == 0 and j == 0:
            maior = menor = num
        if num > maior:
            maior = num
            pos_maior = (i, j)
        if num < menor:
            menor = num
            pos_menor = (i, j)

    # Adicionando a linha à matriz
    matriz.append(linha)

# Mostrando a matriz, maior e menor elementos com suas posições
print("Matriz 6x3:")
for linha in matriz:
    print(linha)

print(f'Maior elemento: {maior} na posição {pos_maior}')
print(f'Menor elemento: {menor} na posição {pos_menor}')

# Fim do programa