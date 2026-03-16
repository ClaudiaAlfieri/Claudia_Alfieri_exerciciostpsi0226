
#Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, divisões, multiplicações e no fim por meio de um acumulador diga quantas operações foram efetuadas. Exemplo introduzindo o número 60 o programa deve apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.

numero = int(input("Insira um número: "))
operacoes = 0  

for i in range(1, numero):  
    print(numero, "+", i, "=", numero + i)
    print(numero, "-", i, "=",numero - i)
    print(numero, "x", i, "=",numero * i)
    print(numero, "/", i, "=",numero / i)
    operacoes += 4  
    
print("\nTotal de operações efetuadas: ", operacoes)
