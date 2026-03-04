
#  Uma loja oferece descontos de acordo com o valor da compra:
# 10% para compras até 200,00€.
# 15% para compras entre 200,01€ e 500,00€.
# 20% para compras acima de 500,00€.
#  Desenvolva um Programa que leia o nome do cliente e o valor da compra e mostre o valor do desconto e o valor total a pagar.

nome=input("Qual é o seu nome?")
valor=float(input("Insira o valor da compra"))

if valor<=200:
    desconto=0.1*valor
elif valor>500:
    desconto=0.2*valor
else:
    desconto=0.15*valor
    
total=valor-desconto
    
    
print(f"Nome: {nome} \n Compra: {valor} \n Desconto: {desconto} \n Total a pagar: {total}")