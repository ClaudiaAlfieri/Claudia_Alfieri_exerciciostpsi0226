#Exception é um erro que ocorre e existe uma necessidade de tratar o mesmo.

#total=10/0  #ZeroDivisionError

#num=int("abc") #ValueError - int só aceita números
#base 8 01234567
#base 16 0123456789abcdef
#base 2 01
#base 10 0123456789

char=str(1)
print(char)

print(ord("1")) #na tabela ASCII, o número 1 tem o código 49
print(chr(49)) #chr() é a função inversa de ord(), ou seja, recebe um código ASCII e retorna o caractere correspondente.

lista = [1,2,3]
#print(lista[4]) #IndexError - a lista tem apenas 3 elementos, então o índice 4 é inválido


#Exemplo de tratamento de exceção usando try-except:

n1=int(input("Insira um número: "))
try:
    total=10/n1
except:
    print("Erro: Divisão por zero não é permitida. Temos um ZeroDivisionError")
    

string=input("introduza um int")

try:
    #resultado=int(string)
    #print(lista[4] )
    pass
except ValueError as erro:
    print("O erro é ", erro)
# except IndexError as erro:
#     print("Index error: ", erroindex)
else:
    print("Não existe erro")
    
idade=10
try:
    if idade <0:
        raise ValueError("Idade não pode ser negativa")
    else:
        print("Idade certa")
except ValueError as erroIdade:
    print(erroIdade)
finally:
    print("Fim do programa")
        
try:
    result=int("string")
    lista[4]
except ValueError as erroIdade:
    print(erroIdade)
finally:
    print("erro de valor")