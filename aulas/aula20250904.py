'''
Curso Python 3 - Softex
Aula do dia: 04/09/2025
Tema: Listas e Laços de Repetição

Lista é um conjunto de valores, que podem ser de tipos diferentes.
Vetor é um conjunto de valores do mesmo tipo.
'''

# Elaborar um programa que leia vários números e mostre eles na ordem inversa:
numeros = []
while True:
    n = int(input("Digite um número (ou -1 para sair): "))
    if n == -1:
        break
    numeros.append(n)

print("Números na ordem inversa:")
for num in reversed(numeros):
    print(num) 
#for num in numeros[::-1]:
#    print(num)
# Outra forma de fazer a inversão é usando o método reverse()
# numeros.reverse()
# print(numeros)
# Outra forma de fazer a inversão é usando o método sort() com o parâmetro reverse=True
# numeros.sort(reverse=True)
# print(numeros)
# Outra forma de fazer a inversão é usando o método sorted() com o parâmetro reverse=True
# print(sorted(numeros, reverse=True))
# Outra forma de fazer a inversão é usando o método pop() dentro de um laço while
# while numeros:
#     print(numeros.pop())
# Outra forma de fazer a inversão é usando o método insert() dentro de um laço for
# numeros_invertidos = []
# for num in numeros:
#     numeros_invertidos.insert(0, num)
# print(numeros_invertidos)
# Outra forma de fazer a inversão é usando o método extend() dentro de um laço for
# numeros_invertidos = []
# for num in numeros:
#     numeros_invertidos = [num] + numeros_invertidos
# print(numeros_invertidos)
# Outra forma de fazer a inversão é usando o método join() dentro de um laço for
# print(' '.join(str(num) for num in numeros[::-1]))
# Outra forma de fazer a inversão é usando o método map() dentro de um laço for
# print(' '.join(map(str, numeros[::-1])))
# Outra forma de fazer a inversão é usando o método reduce() dentro de um laço for
# from functools import reduce
# print(reduce(lambda x, y: str(y) + ' ' + x, numeros[::-1], ''))
# Outra forma de fazer a inversão é usando o método enumerate() dentro de um laço
# for i, num in enumerate(numeros[::-1]):
#     print(num)
# Outra forma de fazer a inversão é usando o método zip() dentro de um laço
# for num in zip(numeros[::-1]):
#     print(num[0])
# Outra forma de fazer a inversão é usando o método filter() dentro de um laço
# for num in filter(lambda x: True, numeros[::-1]):
#     print(num)
# Outra forma de fazer a inversão é usando o método list() dentro de um laço
# for num in list(numeros[::-1]):
#     print(num)
# Outra forma de fazer a inversão é usando o método copy() dentro de um laço
# numeros_invertidos = numeros.copy()
# numeros_invertidos.reverse()
# for num in numeros_invertidos:
#     print(num)
# Outra forma de fazer a inversão é usando o método slice() dentro de um laço
# for num in slice(numeros[::-1]):
#     print(num)
# Outra forma de fazer a inversão é usando o método array() dentro de um laço
# import array
# numeros_array = array.array('i', numeros)
# for num in numeros_array[::-1]:
#     print(num)
# Outra forma de fazer a inversão é usando o método deque() dentro de um laço
# from collections import deque
# numeros_deque = deque(numeros)
# numeros_deque.reverse()
# for num in numeros_deque:
#     print(num)
# Outra forma de fazer a inversão é usando o método numpy() dentro de um laço
# import numpy as np
# numeros_np = np.array(numeros)
# for num in numeros_np[::-1]:
#     print(num)
# Outra forma de fazer a inversão é usando o método pandas() dentro de um laço
# import pandas as pd
# numeros_pd = pd.Series(numeros)
# for num in numeros_pd[::-1]:
#     print(num)
# Outra forma de fazer a inversão é usando o método itertools() dentro de um laço
# import itertools
# for num in itertools.islice(reversed(numeros), len(numeros)):
#     print(num)
# Outra forma de fazer a inversão é usando o método recursion() dentro de uma função
# def print_reversed(lst):
#     if not lst:
#         return
#     print(lst[-1])
#     print_reversed(lst[:-1])
# print_reversed(numeros)
# Outra forma de fazer a inversão é usando o método stack() dentro de um laço
# stack = []
# for num in numeros:
#     stack.append(num)
# while stack:
#     print(stack.pop())
# Outra forma de fazer a inversão é usando o método queue() dentro de um laço
# from queue import LifoQueue
# queue = LifoQueue()
# for num in numeros:
#     queue.put(num)
# while not queue.empty():
#     print(queue.get())
# Outra forma de fazer a inversão é usando o método string() dentro de um laço
# numeros_str = ''.join(str(num) + ' ' for num in numeros)
# print(numeros_str[::-1])
# Outra forma de fazer a inversão é usando o método format() dentro de um laço
# for num in numeros[::-1]:
#     print("Número: {}".format(num))
# Outra forma de fazer a inversão é usando o método f-string dentro de um laço
# for num in numeros[::-1]:
#     print(f"Número: {num}")
# Outra forma de fazer a inversão é usando o método lambda dentro de um laço
# for num in map(lambda x: x, numeros[::-1]):
#     print(num)
# Outra forma de fazer a inversão é usando o método comprehension dentro de um laço
# for num in [num for num in numeros[::-1]]:
#     print(num)
# Outra forma de fazer a inversão é usando o método generator dentro de um laço
# for num in (num for num in numeros[::-1]):
#     print(num)
# Outra forma de fazer a inversão é usando o método itertools.chain() dentro de um laço
# import itertools
# for num in itertools.chain(numeros[::-1]):
#     print(num)
# Outra forma de fazer a inversão é usando o método itertools.cycle() dentro de um laço
# import itertools
# for num in itertools.cycle(numeros[::-1]):
#     print(num)
# Outra forma de fazer a inversão é usando o método itertools.permutations() dentro de um laço
# import itertools
# for num in itertools.permutations(numeros[::-1], 1):
#     print(num[0])
''''''
