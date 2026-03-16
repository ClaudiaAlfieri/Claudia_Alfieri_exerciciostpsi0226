
#Elabore um programa que lê um número e escreve quantos divisores ele possui.

numero = int(input("Insira um número: "))

contagem = 0

for i in range(1, numero + 1):  
    if numero % i == 0:            
        contagem = contagem + 1

print("O número " + str(numero) + " tem " + str(contagem) + " divisores")