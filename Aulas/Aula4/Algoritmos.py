
nomes=[]

#1 - Inserir nome
def insert(nomesi):
    nomesi.append(input("Digite o nome a inserir: "))

#2 - Listar nome
def listar(nomesl):
    for nome in nomesl:
        print(" Nome: ",nome)

#3 - Eliminar nome
def delete(nomesd:list):
 nomesd.pop(int(input("Insert posição")))
 

while True:
    print("1 - Inserir nome")
    print("2 - Listar nome")
    print("3 - Eliminar nome")
    print("4 - Sair")
    opt=input("Escolha uma opção: ")
    match opt :
        case "1":
            insert(nomes)
            print(nomes)          
        case "2":
            listar(nomes)          
        case "3":
            delete(nomes)          
        case "4":
            print("Fim do programa")
            break
        case _: #Default
            print(" Não escolheu a opção certa")