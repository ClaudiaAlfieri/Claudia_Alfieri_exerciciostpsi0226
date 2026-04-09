# 4. Ordenar uma lista de palavras pela quantidade de letras minúsculas
#  Objetivo: Contar quantas letras minúsculas há em cada palavra e ordená-las do menor para o maior número.
# Exemplo:
# ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
# Resultado esperado:
# ["CÓDIGO", "intELIGENTE", "PYthon", "dados", "banana"]
# Como fazer:
# •	Conta, para cada palavra, quantos caracteres estão entre 'a' e 'z'.
# •	Usa esse número como "peso" para ordenar.
# •	Palavras com mais minúsculas vão para o fim da lista.

def contar_minusculas(palavra):
    count = 0
    for char in palavra:
        if 'a' <= char <= 'z':
            count += 1
    return count

def ordenar_por_minusculas(palavras):
    for i in range(len(palavras)):
        for j in range(i + 1, len(palavras)):
            if contar_minusculas(palavras[i]) > contar_minusculas(palavras[j]):
                palavras[i], palavras[j] = palavras[j], palavras[i]
    return palavras

print(ordenar_por_minusculas(["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]))