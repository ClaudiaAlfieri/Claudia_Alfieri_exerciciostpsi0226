# 5. Agrupar palavras pela letra inicial e ordenar cada grupo por ordem alfabética (A → Z)
# Objetivo: Reorganizar as palavras em grupos que comecem com a mesma letra, e depois ordenar cada grupo manualmente.
# Exemplo:
# ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
# Resultado esperado:
# {
#   'b': ['banana', 'bola'],
#   'a': ['abacaxi', 'arroz'],
#   'u': ['urso', 'uva']
# }
# Como fazer:
# •	Cria um dicionário onde cada chave é uma letra inicial.
# •	Coloca cada palavra no grupo correspondente.
# •	Ordena cada grupo individualmente usando comparação com ord().
# Este é o exercício mais completo: vais precisar de organizar, comparar e ordenar em dois níveis.

def agrupar_e_ordenar(palavras):
    grupos = {}
    
    for palavra in palavras:
        letra_inicial = palavra[0].lower()
        if letra_inicial not in grupos:
            grupos[letra_inicial] = []
        grupos[letra_inicial].append(palavra)
    
    for letra in grupos:
        flag = True
        while flag:
            flag = False
            for i in range(len(grupos[letra]) - 1):
                if grupos[letra][i] > grupos[letra][i + 1]:
                    flag = True
                    grupos[letra][i], grupos[letra][i + 1] = grupos[letra][i + 1], grupos[letra][i]
    
    return grupos

print(agrupar_e_ordenar(["banana", "bola", "abacaxi", "arroz", "uva", "urso"]))