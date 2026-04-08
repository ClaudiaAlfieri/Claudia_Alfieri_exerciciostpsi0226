# Exercício 7: Inverter chaves e valores
# Tens o seguinte dicionário:
# d = {'a': 1, 'b': 2, 'c': 3}
# Cria um novo dicionário que tenha os valores como chaves e as chaves como valores. Resultado esperado:
# {1: 'a', 2: 'b', 3: 'c'}


d = {'a': 1, 'b': 2, 'c': 3}

def inverter(dicionario):
    novo = {}
    for chave, valor in dicionario.items():
        novo[valor] = chave
    return novo

print(inverter(d))