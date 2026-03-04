
# Recebe uma operação (em texto) e dois números.
# Operações válidas: "soma", "subtrai", "multiplica", "divide".

num1 =int(input("Digite um número: "))
num2 =int(input("Digite outro número: "))

operacao = input("Escolha um operação: soma, subtrai, multiplica, divide. ")

if operacao == "soma":
    valor= num1 + num2
    print(f"A soma de {num1} e {num2} é {valor}")
elif operacao == "subtrai":
    valor= num1 - num2
    print(f"A subtração de {num1} e {num2} é {valor}")
elif operacao == "multiplica":
    valor= num1 * num2
    print(f"A multiplicação de {num1} e {num2} é {valor}")
elif operacao == "divide":
    valor= num1 / num2
    print(f"A divisão de {num1} e {num2} é {valor}")