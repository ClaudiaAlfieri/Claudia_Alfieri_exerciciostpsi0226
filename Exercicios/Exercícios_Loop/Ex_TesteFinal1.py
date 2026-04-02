
#Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1 (se é número Primo, Quantos divisores e números perfeitos) o Programa deve validar entradas entre 1 e 30.000, e parar de 10 em 10 valores com instrução para parar ou continuar. No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada. Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo introduzido) deve parar de 20 em 20 valores.


while True:
    print("\nCalculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Tabuada")

    escolha = input("Escolha: ")

    match escolha:

        case "1":
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", a + b)

        case "2":
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", a - b)

        case "3":
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", a * b)

        case "4":
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            print("Resultado:", a / b)

        case "5":

            limite = int(input("Número máximo da tabuada (1 a 1000): "))

            if 1 <= limite <= 1000:

                contador = 0

                for i in range(1, limite + 1):

                    print("\nTabuada do", i)

                    for j in range(1, limite + 1):
                        print(i, "x", j, "=", i * j)

                    contador += 1

                    if contador % 20 == 0:
                        resp = input("Continuar? (s/n): ")
                        if resp != "s":
                            break

            else:
                print("Número inválido")
                 
        case _:
            print("Opção inválida")