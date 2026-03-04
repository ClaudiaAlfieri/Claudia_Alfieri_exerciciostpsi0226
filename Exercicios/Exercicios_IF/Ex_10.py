
#  Leia 10 números e determine quantos são pares e quantos são ímpares.

num1=int(input("Digite o número 1?"))
num2=int(input("Digite o número 2?"))
num3=int(input("Digite o número 3?"))
num4=int(input("Digite o número 4?"))
num5=int(input("Digite o número 5?"))
num6=int(input("Digite o número 6?"))
num7=int(input("Digite o número 7?"))
num8=int(input("Digite o número 8?"))
num9=int(input("Digite o número 9?"))
num10=int(input("Digite o número 10?"))

numeros_pares = 0

if num1 % 2 == 0: numeros_pares += 1
if num2 % 2 == 0: numeros_pares += 1
if num3 % 2 == 0: numeros_pares += 1
if num4 % 2 == 0: numeros_pares += 1
if num5 % 2 == 0: numeros_pares += 1
if num6 % 2 == 0: numeros_pares += 1
if num7 % 2 == 0: numeros_pares += 1
if num8 % 2 == 0: numeros_pares += 1
if num9 % 2 == 0: numeros_pares += 1
if num10 % 2 == 0: numeros_pares += 1

numeros_impares = 10 - numeros_pares

print(f"Pares: {numeros_pares} \n Ímpares: {numeros_impares}")

