# Exercício 3 Lista Classes:

class CodigoPostal:
    # Método Construtor:
    def __init__(self, indicativo: int, extensao: int = 000, zona: str = "Indisponível"): 
        self.__indicativo = indicativo
        self.__extensao = extensao
        self.__zona = zona

    # Métodos getters:
    def getIndicativo(self):
        return self.__indicativo
    
    def getExtensao(self):
        return self.__extensao
    
    def getZona(self):
        return self.__zona
    
    # Métodos setters:
    def setIndicativo(self, indicativo: int):
        self.__indicativo = indicativo 
    
    def setExtensao(self, extensao: int):
        self.__extensao = extensao
    
    def setZona(self, zona: str):
        self.__zona = zona

    # Método que exibe o código postal:
    def __str__(self):
        return f'Código Postal: {self.__indicativo}-{self.__extensao} | Zona: {self.__zona}'
    
# Programa que testa a classe:
if __name__ == "__main__":
    # Cria dois objetos:
    cp1 = CodigoPostal(4000)
    cp2 = CodigoPostal(5000, 123, "Porto")

    # Mostra os dados dos objetos:
    print('=== Código Postal 1 ===')
    print(str(cp1))
    print("Indicativo = ", cp1.getIndicativo())
    print("Extensão = ", cp1.getExtensao())
    print("Zona = ", cp1.getZona())

    print("")

    # Mostra os dados dos objetos:
    print('=== Código Postal 2 ===')
    print(str(cp2))
    print("Indicativo = ", cp2.getIndicativo())
    print("Extensão = ", cp2.getExtensao())
    print("Zona = ", cp2.getZona())

    print("########")

    # Vamos pedir para o usuário entrar com os valores do cp:
    print("Digite os valores do Código Postal 3:")
    ind = int(input("Indicativo: "))
    ext = int(input("Extensão: "))  
    zona = input("Zona: ")
    cp3 = CodigoPostal(ind, ext, zona)
    print(str(cp3))

    print("########")

    # Cria um laço de repetição para que o usuário possa criar vários códigos postais diferentes
    # e os armazene em uma dicionário até que ele decida parar de criar ao digitar -1 no indicativo.
    
    codigos_postais = {}
    while True:
        print("Digite os valores do Código Postal (ou -1 para sair):")
        
        ind = int(input("Indicativo: "))
        if ind == -1:
            break
        
        ext = int(input("Extensão: "))  
        zona = input("Zona: ")
        
        cp = CodigoPostal(ind, ext, zona)
        
        codigos_postais[ind] = cp
        
        print("Código Postal adicionado com sucesso!")
        print("")

    print("Você criou os seguintes códigos postais:")
    for ind, cp in codigos_postais.items():
        print(str(cp))

    print("########")