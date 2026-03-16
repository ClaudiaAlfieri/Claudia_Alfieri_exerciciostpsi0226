
#Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. Validando a entrada de números inteiros entre 1 e 50.

soma = 0
contador = 0

while contador < 30:
    numero = int(input("Digite um número par entre 1 e 50: "))

    if numero >= 1 and numero <= 50 and numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
    else:
        print("Número inválido! Tente novamente.")

media = soma / 30

print("A média dos números é:", media)