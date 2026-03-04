
# Recebe um dicionário com as chaves "status" e "tempo_resposta".
# Retorna:
# •	“Servidor ativo” se o status for “ok”
# •	“Servidor lento” se o status for “ok” e o tempo de resposta for maior que 200 ms
# •	“Servidor indisponível” se o status for “erro”
# •	“Estado desconhecido” caso contrário


print("1 - Status ok")
print("2 - Status erro")

opc = input("Escolha uma opção: ")

match opc:
    case "1":        
        tempo = float(input("Qual é o tempo de resposta? "))
        if tempo>200:
            print("Servidor lento")
        else:
            print("Servidor ativo")
    case "2":      
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")