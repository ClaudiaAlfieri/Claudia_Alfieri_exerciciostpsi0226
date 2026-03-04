
# Recebe um dicionário com as chaves "categoria" e "preco".
# Retorna:
# •	“Produto de luxo” se categoria for “eletrônico” e preço acima de 1000
# •	“Produto comum” se categoria for “eletrônico” e preço até 1000
# •	“Produto alimentar” se categoria for “alimento”
# •	“Categoria desconhecida” caso contrário

print("1 - Eletrônico")
print("2 - Alimento")

opc = input("Escolha uma opção: ")

match opc:
    case "1":        
        valor = float(input("Qual é o preço do produto? "))
        if valor>1000:
            print("Produto de luxo")
        else:
            print("Produto comum")
    case "2":      
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")