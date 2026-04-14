# Dimensões:
    
#     0   1    2    3
#     1   1    50   20
#     2   45   30   60
#     3   70   80   90
    
    
#     Para acessar o número 45 vc faz:
        
#     lista [1] [2]

#Conrolo de fluxe #"Loop" a uma dimensão

# listanum = [9, 2, 4, 8, 6, 1]
#index      0  1  2  3  4  5

#varaux=1
# varaux=listanum[5]

# #listanum[5]=9
# listanum[5] = listanum[0]

# listanum=[9,2,4,8,6,9]
# #listanum[0]= 1
# listanum[0] = varaux

# listanum=[1,2,4,8,6,9]

# #if
# listanum[i] > listanum[i+1]

listanum = [9, 2, 4, 8, 6, 1]
#index      0  1  2  3  4  5

flags= True

#bubble sort - ordenação de uma lista de números usando o método de comparação e troca

while flags:
    flags = False
    print("Loop de fora")
    for i in range(len(listanum)-1):
        print("Loop interior")
        print("i: ", i)  
        if listanum[i] > listanum[i+1]:
            flags = True
            print("troca aconteceu","posição i", listanum[i], "posição i+1", listanum[i+1])
            listanum[i], listanum[i+1] = listanum[i+1], listanum[i]            
print(listanum)