
#Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial 6=3+2+1 .

numero = int(input("Digite um número: "))
quantidade = 0

for num in range(1, numero + 1):

    soma = 0

    for divisor in range(1, num):
        if num % divisor == 0:
            soma = soma + divisor

    if soma == num:
        print(num, "É um número perfeito")
        quantidade = quantidade + 1

print("Quantidade de números perfeitos:", quantidade)