'''Exercício 26: Na teoria dos sistemas define-se o elemento MINMAX de uma matriz como sendo o maior
elemento da linha onde se encontra o menor elemento da matriz. Faça um algoritmo que leia uma matriz
4 x 7 com números reais de 0 a 10, calcule e mostre seu MINMAX e sua posição (linha e coluna).
'''

import random

# Inicializando a matriz 4x7
matriz = []
minimo = float('inf') # Inicialmente, o menor valor é infinito
pos_minimo = (0, 0) # Posição do menor elemento
minmax = None
pos_minmax = (0, 0) # Posição do elemento MINMAX

# Preenchendo a matriz com números aleatórios entre 0 e 10
for i in range(4):
    linha = []
    for j in range(7):
        num = random.uniform(0, 10) # Gerando número real entre 0 e 10
        linha.append(num)
        # Verificando se é o menor elemento
        if num < minimo:
            minimo = num
            pos_minimo = (i, j)
    matriz.append(linha)

# Encontrando o MINMAX na linha do menor elemento
linha_minimo = pos_minimo[0]
minmax = max(matriz[linha_minimo])
pos_minmax = (linha_minimo, matriz[linha_minimo].index(minmax))

# Mostrando a matriz
print("Matriz 4x7:")
for linha in matriz:
    print(['{:.2f}'.format(num) for num in linha])

# Mostrando o menor elemento e sua posição
print(f'Menor elemento: {minimo:.2f} na posição {pos_minimo}')
# Mostrando o MINMAX e sua posição
print(f'MINMAX: {minmax:.2f} na posição {pos_minmax}')

# Fim do programa
