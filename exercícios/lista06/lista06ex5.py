'''
Faça um algoritmo que carregue uma matriz 12 x 4 com os valores das vendas de uma loja, onde cada
linha representa um mês do ano e cada coluna representa uma semana do mês. Calcule e mostre:
• o total vendido em cada mês do ano, mostrando o nome do mês por extenso;
• o total vendido em cada semana durante todo o ano;
• o total vendido pela loja no ano.
'''

# Início do programa

# Inicia a matriz:
vendas = []

# Preenchendo a matriz vendas

for mes in range (12):
    print("Estamos no mês: ", mes + 1)
    print("Digite os valores das vendas por semana.")
    
    for semana in range(4):
        # Solicita o valor das vendas da semana:
        valor = float(input(f"Digite o valor de vendas da semana {semana + 1}: R$ "))
        if len(vendas) <= mes:
            vendas.append([])
        vendas[mes].append(valor)
        
# Calcula o total vendido em cada mês do ano:
nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
totais_meses = []