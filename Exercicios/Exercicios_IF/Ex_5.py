
# Ler 3 valores inteiros e apresentar os valores dispostos em ordem crescente e decrescente.

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


meio = num1 + num2 + num3 - maior - menor

print(f"Crescente: {menor}, {meio}, {maior}")
print(f"Decrescente: {maior}, {meio}, {menor}")