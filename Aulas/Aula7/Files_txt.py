
# Qualquer ação que se façacom ficheiros
# read, write, append, binario

# 1 - Open file
# 2 - Acção
# 3 - Close file

# ./ = na mesma pasta
# ../ = pasta acima

filename = "./Claudia_Alfieri_exerciciostpsi0226/Aulas/Aula7/Dados/data.txt"

# # Para ler o arquivo "r"

# with open(filename,"r", encoding="utf-8") as manipfile:
#     texto=manipfile.read()
#     print("no file", texto)

# # Para escrever no arquivo "w"

# texto=input("Introduza uma frase: ")

# with open(filename,"w", encoding="utf-8") as manipfile:
#     manipfile.write(texto)  
    
#Quando o arquivo não existe:
Texto=""
opcao=0

import os as fsos

# Cria o ficheiro se não existir
if fsos.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as manipfile:
         texto = manipfile.read()
         
while True:
    
    print("1 - Para escrever no texto")
    print("2 - Para listar o texto")
    print("3 - Para gravar no file")
    print("4 - Para sair do programa")
    opcao=int(input("Escolha uma opção: "))
    
    match opcao:
        case 1:
            texto = input("Introduza uma frase: ")
        case 2:
            print(texto)
        case 3:
             with open(filename, "w", encoding="utf-8") as manipfile:
                 manipfile.write(texto)
        case 4:
            guarda = input("Deseja guardar o texto antes de sair? (s/n): ")
            if guarda == "s" or guarda == "S":
                with open(filename, "w", encoding="utf-8") as manipfile:
                    manipfile.write(texto)
            break


 

