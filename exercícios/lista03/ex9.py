'''
Elabora um algoritmo que dada a idade de um nadador classifica-o
em uma das seguintes categorias:
- infantil A = 5 a 7 anos
- infantil B = 8 a 10 anos
- juvenil A = 11 a 13 anos
- juvenil B = 14 a 17 anos
- adulto = maiores de 18 anos
'''

# Início do programa
def recebe_idade(mensagem, minimo=0):
    # Recebe e valida uma idade positiva do usuário
    while True:
        try:
            idade = int(input(mensagem))
            if idade >= minimo:
                return idade
            else:
                print(f"A idade deve ser maior ou igual a {minimo}. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido.")

def classifica_nadador_ifelse(idade):
    # Classifica o nadador com base na idade usando if-else:
    if 5 <= idade <= 7:
        return "Infantil A"
    elif 8 <= idade <= 10:
        return "Infantil B"
    elif 11 <= idade <= 13:
        return "Juvenil A"
    elif 14 <= idade <= 17:
        return "Juvenil B"
    elif idade >= 18:
        return "Adulto"
    else:
        return "Idade fora do intervalo de classificação"
    
def classifica_nadador_match(idade):
    # Classifica o nadador com base na idade usando match-case
    match idade:
        case idade if 5 <= idade <= 7:
            return "Infantil A"
        case idade if 8 <= idade <= 10:
            return "Infantil B"
        case idade if 11 <= idade <= 13:
            return "Juvenil A"
        case idade if 14 <= idade <= 17:
            return "Juvenil B"
        case _ if idade >= 18:
            return "Adulto"
        case _:
            return "Idade fora do intervalo de classificação"
        
def main():
    print("===== Classificação de Nadador =====")
    idade = recebe_idade("Digite a idade do nadador: ", minimo=0)

    # Usando if-else
    categoria_ifelse = classifica_nadador_ifelse(idade)
    print(f"Classificação (if-else): {categoria_ifelse}")

    # Usando match-case
    categoria_match = classifica_nadador_match(idade)
    print(f"Classificação (match-case): {categoria_match}")

if __name__ == "__main__":
    main()

# Fim do programa