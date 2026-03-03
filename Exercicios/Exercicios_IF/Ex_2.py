
# Desenvolva um programa que analise 3 numores inteiros e informe qual o maior e qual o menor deles.

num1=int(input("Insira um número"))
num2=int(input("Insira outro número"))
num3=int(input("Insira mais um número"))


if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")