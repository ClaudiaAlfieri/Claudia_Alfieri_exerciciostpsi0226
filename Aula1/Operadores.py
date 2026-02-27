#Operadores Aritméticos

#soma +, sub -, div /, mult *, mode % (resto da div), exponencial **

total=0
num1=0
num2=0

#input values
num1=int(input("Insira num 1"))
num2=int(input("Insira num 2"))

total=num1+num2
print(f"Soma : {total}")

total=num1-num2
print("Subtração : ", total , ".")

total=num1/num2
print(f"Divisão : {total}")

total=num1*num2
print("Multiplicação : ", total , ".")

#Operadores de Decisão

# == igualdade, != diferente, > maior que, < menor que
# >= maior ou igual e  <= menor ou igual

#expressão
#val1 == val2   = True/False

#Operadore Lógicos

#and (&&) e or (||)

#expressão
#val1 > val2 and val2 > val3 = true/false
#   true     and    false    = false


#Exercício encontra o maior e o menor
#IF

val1=2
val2=3
val3=4

if val1>val2 and val2>val3:
    print("val1 é o maior, val3 é o menor")
elif val2>val1 and val1>val3:
    print("val2 é o maior, val3 é o menor")
elif val3 > val1 and val1 > val2:
    print("val3 é o maior, val1 é o menor")
elif val1 > val3 and val3 > val2:
    print("val1 é o maior, val2 é o menor")
elif val2 > val3 and val3 > val1:
    print("val2 é o maior, val1 é o menor")
elif val3 > val2 and val2 > val1:
    print("val3 é o maior, val1 é o menor")