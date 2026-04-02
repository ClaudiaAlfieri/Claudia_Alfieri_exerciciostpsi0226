# Exercício 5: Contar letras numa palavra
# Pede ao utilizador que introduza uma palavra. Em seguida, cria um dicionário onde cada letra da palavra é uma chave e o seu valor é o número de vezes que essa letra aparece.
# Exemplo de entrada: "banana"
# Resultado esperado: {'b': 1, 'a': 3, 'n': 2}
# # Saída: {'b': 1, 'a': 3, 'n': 2}

palavra = input("Digite uma palavra: ")
contagem = {}

for letra in palavra:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)
