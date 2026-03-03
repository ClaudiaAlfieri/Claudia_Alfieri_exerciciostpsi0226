
#  Desenvolva um Programa que leia o saldo inicial de um cliente de banco e leia também o valor de um cheque. Analise se o cheque pode ser descontado. Se o cheque não puder ser descontado, mostre essa informação, caso contrário, desconte o cheque e informe o saldo atualizado.

saldo=float(input("Insira o saldo inicial da conta"))
cheque=float(input("Insira o valor do cheque"))

if saldo>cheque:
    print(f"Cheque descontado, saldo {saldo - cheque}")
else:
    print(f"Saldo insuficiente")