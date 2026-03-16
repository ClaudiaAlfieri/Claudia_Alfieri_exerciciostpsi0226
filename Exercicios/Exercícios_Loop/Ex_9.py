
#Escreva um programa que solicite um número ao utilizador até que o valor deste esteja entre os valores 1 e 100.(Use o ciclo do ... while)

  
numero = int(input("Insira um número: "))

while numero < 1 or numero > 100:    
    numero = int(input("Insira um outro número ")) 

print("Número válido:", numero)