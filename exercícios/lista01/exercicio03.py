'''
Este exercício deve receber a idade de uma pessoa em dias e converter para anos, meses e dias.
O programa deve tratar a entrada para garantir que o usuário digite um número inteiro positivo.
'''

# Inicio do programa
def converter_idade(dias):
    anos = dias // 365
    meses = (dias % 365) // 30
    dias_restantes = (dias % 365) % 30
    return anos, meses, dias_restantes

def ler_idade_em_dias():
    while True:
        try:
            dias = int(input("Digite a idade em dias: "))
            if dias < 0:
                print("A idade em dias não pode ser negativa. Tente novamente.")
            else:
                return dias
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def main():
    print("Conversor de Idade em Dias")
    print(f"====================================")
        
    # Ler idade em dias
    dias = ler_idade_em_dias()
    
    # Converter para anos, meses e dias
    anos, meses, dias_restantes = converter_idade(dias)
    
    # Exibir resultado
    print(f"Idade: {anos} anos, {meses} meses e {dias_restantes} dias.")

if __name__ == "__main__":
    main()

# Fim do programa