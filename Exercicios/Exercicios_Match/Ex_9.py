
# Recebe um dicionário com as chaves "metodo" e "conteudo".
# Retorna:
# •	“Requisição GET recebida” se o método for “GET”
# •	“Requisição POST com dados válidos” se o método for “POST” e o conteúdo não estiver vazio
# •	“Requisição POST sem dados” se o método for “POST” e o conteúdo estiver vazio
# •	“Método não suportado” caso contrário

print("1 - Get")
print("2 - Post")

opc = input("Escolha uma opção: ")

match opc:
    case "1":        
        print("Requisição GET recebida")
    case "2": 
        dados =input("Existem dados válidos? ")
        if dados == "sim":
            print("Requisição POST com dados válidos")
        else:
            print("Requisição POST sem dados")            
    case _:
        print("Método não suportado")
