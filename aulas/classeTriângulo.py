# Aula 18/09/2025
# Assunto: Programação Orientada a Objetos (POO) em Python

# Definição de uma classe Triângulo
class Triangulo:
    # Método construtor (Utilizado para criar objeto)
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    # Método para calcular a área:
    def area(self):
        return (self.__base * self.__altura)/2
    
    def perimetro(self):
        return (self.__base + self.__altura) * 2

    def __str__(self):
        return f"Triangulo tem base {self.__base} e altura {self.__altura}"