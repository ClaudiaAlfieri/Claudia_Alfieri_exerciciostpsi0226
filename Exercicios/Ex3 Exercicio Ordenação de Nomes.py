# Ordenação de Nomes com Base na Tabela ASCII
# Recebeste uma lista com nomes completos de várias pessoas. A tua tarefa é ordená-los alfabeticamente, considerando o primeiro nome como critério principal e o apelido como critério de desempate, com base nos valores ASCII dos caracteres.
# Lista de Nomes:
# nomes = [
#     "Pedro Pereira",
#     "Ana Beatriz",
#     "Ana Clara",
#     "Carlos Silva",
#     "Beatriz Souza",
#     "Ana Paula",
#     "Pedro Andrade"
# ]
# Regras:
# 1.	Ordena os nomes primeiro pelo primeiro nome comparando Caractere a Caractere.
# 2.	Se houver mais do que uma pessoa com o mesmo primeiro nome, usa o apelido como critério de desempate comparando Caractere a Caractere.
# 3.	Utiliza os valores ASCII implícitos na ordenação padrão de strings em Python (sem recorrer a bibliotecas).
# Resultado Esperado:
# Depois de ordenares, a lista deve ficar assim:
# [
#     "Ana Beatriz",
#     "Ana Clara",
#     "Ana Paula",
#     "Beatriz Souza",
#     "Carlos Silva",
#     "Pedro Andrade",
#     "Pedro Pereira"
# ]


nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade"
]

# Função que retorna uma "chave de ordenação" para cada nome
# Separa o nome completo em [primeiro_nome, apelido]
# Primeiro compara o 1º elemento,
# se for igual, compara o 2º
def chave_ordenacao(nome_completo):
    partes = nome_completo.split(" ")  
    primeiro_nome = partes[0]       
    apelido = partes[1]               
    return (primeiro_nome, apelido)   


nomes_ordenados = sorted(nomes, key=chave_ordenacao)

print(nomes_ordenados)