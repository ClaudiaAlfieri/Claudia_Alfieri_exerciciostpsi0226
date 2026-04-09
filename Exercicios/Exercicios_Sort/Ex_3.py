# 3. Ordenar os caracteres de uma palavra por ordem alfabética
# Objetivo: Pega numa palavra e reorganiza as suas letras da mais "baixa" para a mais "alta", segundo o valor ASCII.
# Exemplo:
# "algoritmo"
# Resultado esperado:
# "agilmootr"
# Como fazer:
# •	Divide a palavra em caracteres.
# •	Ordena os caracteres com base no valor de ord().
# •	Junta novamente numa string.
# Este exercício é útil para aprender como a ordenação funciona mesmo a nível de caracteres, não só de palavras inteiras.

def ordenar_caracteres(palavra):
    caracteres = list(palavra)
    for i in range(len(caracteres)):
        for j in range(i + 1, len(caracteres)):
            if caracteres[i] > caracteres[j]:  
                caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
    return ''.join(caracteres)

print(ordenar_caracteres("algoritmo"))
