# Arquivo main para testar as classes da Lista 01

# Importa a classe Retângulo do arquivo ex2.py
from ex2 import Retangulo

# Cria um objeto:
r1 = Retangulo()
r2 = Retangulo(2, 5)

# Mostra os dados dos objetos:
print('=== Triangulo 1 ===')
print(str(r1))
print("Aréa = ", r1.area())
print("Perímetro = ", r1.perimetro())
print("Relação = ", r1.relacao())

if r1.ehQuadrado():
    print("É um quadrado")
else:
    print("Não é um quadrado")

print("")
# Mostra os dados dos objetos:
print('=== Triangulo 2 ===')
print(str(r2))
print("Aréa = ", r2.area())
print("Perímetro = ", r2.perimetro())
print("Relação = ", r2.relacao())

if r2.ehQuadrado():
    print("É um quadrado")
else:
    print("Não é um quadrado")

print("########")