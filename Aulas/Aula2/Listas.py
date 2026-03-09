#Listas em inteiros trocas

numeros= [1,5,8,3,9,23]
#index D1 0 1 2 3 4 5

for numero in numeros:
    print(numero)
numeros[2]=6

for numero in numeros:
    print(numero)
    
#Lista de strings

nomes  = ["Joao", "Pedro", "Antonio"]
# index D2 0123    01234    0123456

for nome in nomes:
    print(nomes)
    
    # print("Olá","mundo", end="/t", sep="        ")
    # print("", end="/n/n/n")
        
    nomes[0]="Thiago"
    print(nomes[0][2])
    
    #1 Quantas dimensões realmente tem? 2 dimensões.
    #2 Como adicionar mais elemenstos?
    #3 Como remover elementos?
    # == compara unicode da string completa
    
    print("", end="\n\n\n")
    
    print(nomes)
    
    # Como remover elementos?
    # Procura:
    nomes.remove("Pedro")
    print(nomes) 
    
    #Por indice:
    nomes.pop(0)
    print(nomes)
    
    #Adicionar elemento:    
    nomes.append("Dario")
    print(nomes)
    print(nomes.count("Dario"))
    
    print(nomes)
    print(len(nomes))
    print(nomes.index('Antonio'))
 
    