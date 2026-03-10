#Dicionarios

# Dicionário é uma coleção de dados que armazena pares de chave-valor.
# {} = dicionario   -> tem a mesma estrutura de um json

carros={"Marca":"BMW", "Modelos":"M3"}

#Acesso em Mapping:

print(carros["Marca"])
print(carros["Modelos"])

#Alterar um valor do dicionário:
#update() = se não existir a chave, ele cria a chave e o valor, se existir a chave, ele atualiza o valor da chave.

carros.update({"Marca":"Fiat"})
print(carros)

carros={"Marc":"BMW", "Modelos":"M3"}

carros.update({"Marca" : "BMW"})
print(carros)
carros.pop("Marc")
print(carros)

#Outra opção para apagar:
del carros["Modelos"]
print (carros)

