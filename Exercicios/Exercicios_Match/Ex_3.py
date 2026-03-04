
# Recebe um dicionário com as chaves "tipo" e "valor".
# Exibe:
# •	“Compra de X€” se tipo for “compra”
# •	“Venda de X€” se tipo for “venda”
# •	“Pedido desconhecido” caso contrário

print("1 - Compra")
print("2 - Venda")

opc = input("Escolha uma opção: ")

match opc:
    case "1":
        valor = float(input("Quanto quer comprar? "))
        print(f"Compra de {valor}€")
    case "2":
        valor = float(input("Quanto quer vender? "))
        print(f"Venda de {valor}€")
    case _:
        print("Pedido desconhecido")