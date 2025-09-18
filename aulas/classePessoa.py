# Definição da classe pessoa:

class Pessoa:
    # Método construtor:
    def __init__(self, nome = "", numContribuinte = 0, idade = 0):
        self.__nome = nome
        self.__numContribuinte = numContribuinte
        self.__idade = idade

    def __str__(self):
        return f'Nome: {self.__nome}, Numero de Contribuinte: {self.__numContribuinte}, Idade: {self.__idade}'
    
    