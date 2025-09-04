'''
Jogo de Adivinhação de Palavras
O jogador tenta adivinhar uma palavra letra por letra.
'''

palavra = "escola"

letras_acertadas = ['_'] * len(palavra)
tentativas = 6
letras_erradas = []

print("Bem-vindo ao Jogo de Adivinhação de Palavras!")
print("A palavra tem", len(palavra), "letras.")
print("Você tem", tentativas, "tentativas para adivinhar a palavra.")
print(" ".join(letras_acertadas))

while tentativas > 0 and '_' in letras_acertadas:
    letra = input("Digite uma letra: (Digite 0 para sair) ").lower()

    # Condição de saída:
    if letra == '0':
        print("Você saiu do jogo. A palavra era:", palavra)
        break

    # Validação de entrada
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra.")
        continue

    if letra in letras_acertadas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in palavra:
        print("Boa! A letra", letra, "está na palavra.")
        for i, char in enumerate(palavra):
            if char == letra:
                letras_acertadas[i] = letra
    else:
        tentativas -= 1
        letras_erradas.append(letra)
        print("Ops! A letra", letra, "não está na palavra.")
        print("Você tem", tentativas, "tentativas restantes.")

    print(" ".join(letras_acertadas))
    if letras_erradas:
        print("Letras erradas:", ", ".join(letras_erradas))

if '_' not in letras_acertadas:
    print("Parabéns! Você adivinhou a palavra:", palavra)
else:
    print("Fim de jogo! A palavra era:", palavra)

# Fim do jogo