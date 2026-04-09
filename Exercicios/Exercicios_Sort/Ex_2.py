# 2. Ordenar uma lista de palavras por ordem alfabética inversa (Z → A), ignorando maiúsculas/minúsculas
# Objetivo: Reordenar da última letra do alfabeto para a primeira, sem distinguir maiúsculas de minúsculas.
# Exemplo:
# ["Python", "inteligência", "Aprender", "dados", "Rede"]
# Resultado esperado:
# ["Rede", "Python", "inteligência", "dados", "Aprender"]
# Como fazer:
# •	Compara os caracteres em minúsculas ("A" e "a" passam a ser tratados como iguais).
# •	Ordena da última letra para a primeira.
# •	A lógica da comparação será invertida: em vez de colocar as menores primeiro, colocas as maiores.


def ordenar_palavras(palavras):
    for i in range(len(palavras)):
        for j in range(i + 1, len(palavras)):
            if palavras[j].lower() > palavras[i].lower():
                palavras[j], palavras[i] = palavras[i], palavras[j]
    return palavras
print(ordenar_palavras(["Python", "inteligência", "Aprender", "dados", "Rede"]))
