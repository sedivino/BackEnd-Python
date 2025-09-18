'''
Desenvolva uma classe de nome Retangulo cujas variáveis de instância são capazes de guardar
a base e a altura de um retângulo. Suponha que esses valores são do tipo inteiro. Deverão poder
ser criados objetos do tipo Retangulo com quaisquer bases e alturas. Caso estes valores não
sejam indicados os retângulos deverão ser, por padrão, quadrados de lado igual a 1. Cada instância
desta classe deverá ser capaz de responder às seguintes mensagens:
◦ Qual a área do retângulo?
◦ Qual o perímetro do retângulo?
◦ Qual a relação base/altura?
◦ Este retângulo é quadrado?
◦ Mostra as dimensões deste retângulo.
Escreva um programa de teste para a classe Retangulo. Crie dois retângulos de dimensões 1x1 e
2x5, por exemplo, e teste nestes os vários métodos de instância da classe.
'''

# Define a Classe Retângulo:
class Retangulo:
    # Método Construtor:
    def __init__(self, base = 1, altura = 1):
        self.__base = base
        self.__altura = altura
    
    # Método para calcular a área:
    def area(self):
        return (self.__base * self.__altura)
    
    # Método para calcular o perímetro:
    def perimetro(self):
        return (2*self.__altura + 2*self.__base)
    
    # Método para calcular a proporção do retângulo:
    def relacao(self):
        return (self.__base / self.__altura)
    
    # Método para dizer se é um quadrado:
    def ehQuadrado(self):
        return self.__base == self.__altura
    
    # Método que exibe as dimenções do retângulo:
    def __str__(self):
        return f'Retângulo tem base = {self.__base} e altura = {self.__altura}.'    
