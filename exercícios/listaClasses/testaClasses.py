# Arquivo main para testar as classes da Lista 01

# Importa a classe Retângulo do arquivo ex2.py
from ex2 import Retangulo

# Cria um objeto:
r1 = Retangulo()
r2 = Retangulo(2, 5)

print('=== Triangulo 1 ===')
print(str(r1))
print(r1.area())
print(r1.perimetro())
print(r1.relacao())
print(r1.ehQuadrado())
print("")

print('=== Triangulo 2 ===')
print(str(r2))
print(r2.area())
print(r2.perimetro())
print(r2.relacao())
print(r2.ehQuadrado())
