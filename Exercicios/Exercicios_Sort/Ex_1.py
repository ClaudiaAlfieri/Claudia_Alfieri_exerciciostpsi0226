# 1.	Ordenar uma lista de palavras por ordem alfabética (A → Z)
# Objetivo: Reordenar as palavras, comparando carácter por carácter, como se estivesses a fazer o papel da função sorted().
# Exemplo:
# ["banana", "uva", "abacaxi", "laranja"]
# Resultado esperado:
# ["abacaxi", "banana", "laranja", "uva"]
# Como fazer:
# •	Compara as palavras duas a duas.
# •	Usa o código ASCII de cada letra para decidir qual vem antes.
# •	Se duas palavras começarem pela mesma letra, continua a comparação na letra seguinte.
# •	Se uma palavra for prefixo da outra (como "casa" e "casamento"), a mais curta deve vir primeiro.

def ordenar_palavras(palavras):
    flag = True
    
    while flag:
        flag = False
        for i in range(len(palavras) - 1):
            if palavras[i] > palavras[i + 1]:
                flag = True
                palavras[i], palavras[i + 1] = palavras[i + 1], palavras[i]
    
    return palavras

print(ordenar_palavras(["banana", "uva", "abacaxi", "laranja"]))