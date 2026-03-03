
#  Crie 2 variáveis (num1 e num2) e leia o valor para cada uma delas. Mostre os valores de forma crescente e decrescente.

num1=int(input("Insira um número"))
num2=int(input("Insira outro número"))

if num1>num2:
   print(f"Crescente: {num2,num1}")
else:
    print(f"Crescente: {num1,num2}")


if num1>num2:
   print(f"Decrescente: {num1,num2}")
else:   
    print(f"Decrescente: {num2, num1}")
