# Aula do dia 18/09/2025
# Assunto: Programação Orientada a Objetos (POO) em Python

# Módulo que testa os exercícios de classe:
#from classeTriângulo import Triangulo
from classePessoa import Pessoa

'''
t1 = Triangulo (5, 10)
t2 = Triangulo (10, 10)

print("Área de t1: ", t1.area())
print("Área de t2: ", t2.area())
print("Perímetro de t1: ", t1.perimetro())
'''
# Cria o objeto pessoa:
pessoa1 = Pessoa("Joana", 456, 32)
pessoa2 = Pessoa("João", 000, 00)
pessoa3 = Pessoa("Magali")
pessoa4 = Pessoa(numContribuinte=789, idade=40)

print(pessoa1)
print(pessoa2)
print(pessoa3)
print(pessoa4)

