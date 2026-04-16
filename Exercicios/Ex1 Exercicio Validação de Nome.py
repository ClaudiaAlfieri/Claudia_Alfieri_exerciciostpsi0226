# Cria um programa que peça ao utilizador para introduzir o seu nome completo. O programa deve validar se o nome contém apenas letras e espaços, a primeira letra do nome deve ser sempre maiúscula e a seguir ao espaço também, usando os códigos ASCII de cada caractere.
# Exemplo:
# Pedro Pereira 

# Se o nome for válido, o programa deve exibir:
#  "Nome válido!"
# Caso contrário, deve exibir:
#  "Nome inválido: contém caracteres não permitidos."

# No caso de o programa encontrar um caractere invalido deve parar a execução.

# Exemplos Inválidos:
# Miguel PriMo
# Luis AnseLmo
# Guilherme ramos

nome = input("Digite o seu nome: ")
for i in range (len(nome)):
    if nome[i] == " ":
        pass 
      # Maiúsculas: ASCII 65-90 | Minúsculas: ASCII 97-122
    elif 65 <= ord(nome[i]) <= 90 or 97 <= ord(nome[i]) <= 122:
        if i ==0 or nome[i-1] == " ":
            if not (65 <= ord(nome[i]) <= 90):     
                print("Nome inválido: contém caracteres não permitidos.")
                break
        else:
            if not (97 <= ord(nome[i]) <= 122):
                print("Nome inválido: contém caracteres não permitidos.")
                break                     
    else:
        print("Nome inválido: contém caracteres não permitidos.")
        break
else:   
    print("Nome válido!")




 

 



