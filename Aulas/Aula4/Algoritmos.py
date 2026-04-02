nomes=["da","fa","oi","da"]
#index   0    1    2   3

indices = []
 
 #1 - inserir nome
def insert(nomesi:list):
    nomesi.append(input("insert um nome"))
 
 #2 - listar nomes
def listar(nomesl:list):
    for nome in nomesl:
        print("nome : " , nome)
        
 #3 - delete nome
def delete(nomesd:list):
    nomesd.pop( int(input(" insert posiçao ")))
 
 #4 - procurar nome -> retorna a posiçao do nome na lista
#  def procurar(nomesp:list):
#     nome=input("insert nome de procura")
#     for i in range(len(nomesp)):
#         if nomesp[i] == nome:
#             print("nome: ",nomesp[i] ," na posiçao ", i)

#4 - procurar nome -> retorna a posiçao do nome na lista e o nome encontrado dentro do while      

def procurar(nomesprocura:list, indices:list):
    indices.clear()
    nome = input("Insere um nome: ")
    for i in range(len(nomesprocura)):
     if nomesprocura[i] == nome:
         indices.append(i)
    return(indices)



while True:
    print ("1 - inserir nome")
    print ("2 - listar nomes")
    print ("3 - delete nome")
    print ("4 - procurar nome")
    print ("5 - sair")
    opt=input("Escolha Opção")
    match opt :
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
        case "3":
            delete(nomes)
        case "4":
            #  procurar(nomes)
            resultado = procurar(nomes, indices)
            if resultado:
                for i in resultado:
                    print(f"Nome '{nomes[i]}' encontrado na posição {i}")     
                        
        case "5":
            print("fim do programa")
            break
        case _:
            print("nao escolheu a opçao certa")
            
            