
# Crie um algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.

numero = int(input("Insira um número inteiro: "))

primo = True 

if numero < 2:
    print("O número não é primo")

else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
     
    if primo:
        print("O número é primo")
    else:
        print("O número não é primo")