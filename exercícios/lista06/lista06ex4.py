'''
# Faça um algoritmo que receba:
• as notas de 15 alunos em cinco provas diferentes e armazene-as em uma matriz 15 x 5;
• as matrículas dos 15 alunos e armazene-os em um vetor de 15 posições. Calcule e mostre:
    ◦ para cada aluno, a matrícula, a média aritmética das cinco provas e a situação (Aprovado,
Reprovado ou Exame);
    ◦ a média da classe. 
'''
import random

# Criamos uma matriz 15x5 para armazenar as notas dos alunos e um vetor para armazenar as matrículas:
notas = []
matriculas = []

# Preenchemos a matriz de notas e o vetor de matrículas com dados de exemplo:
for i in range(15):
    # Gerando uma matrícula fictícia
    matricula = 1000 + i
    matriculas.append(matricula)
    
    # Gerando notas fictícias para 5 provas
    provas = [random.randint(0, 10) for _ in range(5)]
    notas.append(provas)

# Calculamos a média de cada aluno e a média da classe:
soma_classe = 0
for i in range(15):
    media_aluno = sum(notas[i]) / 5
    soma_classe += media_aluno
    
    # Determinando a situação do aluno
    if media_aluno >= 7:
        situacao = "Aprovado"
    elif media_aluno >= 4:
        situacao = "Exame"
    else:
        situacao = "Reprovado"
    
# Mostrando a matrícula, média e situação do aluno
print(f'Matrícula: {matriculas[i]}, Média: {media_aluno:.2f}, Situação: {situacao}')

# Calculando e mostrando a média da classe
media_classe = soma_classe / 15
print(f'Média da classe: {media_classe:.2f}')

# Fim do programa