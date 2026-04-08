# Exercício 8: Juntar dois dicionários
# Dado os seguintes dicionários:
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# Cria um novo dicionário que contenha os pares chave-valor dos dois dicionários juntos.


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

def juntar(d1, d2):
    novo = {}
    novo.update(d1)
    novo.update(d2)
    print(novo)

juntar(d1, d2)