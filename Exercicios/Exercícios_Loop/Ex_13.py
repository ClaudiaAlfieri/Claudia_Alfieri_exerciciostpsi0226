
#Elabore um programa que leia um número e mostre a tabuada. (multiplicar de 1 a 10)
numero= int(input("Insira um número: "))

for i in range(1,11):
    print(numero, "x", i, "=", numero * i)