import re as reg

texto = "Ola, mundo"
lista = reg.split(",", texto) #separa a string em partes usando a vírgula como delimitador
print(lista)
print(reg.match("Ola", texto)) #procura no inicio da string
print(reg.search("mundo", texto)) #procura em toda a string
print(reg.findall("o", texto)) #procura todas as ocorrências de "o" na string

var=reg.search("mundo", texto) #se a busca for bem-sucedida, var será um objeto de correspondência, caso contrário, será None
var2=reg.findall("o", texto) #var2 será uma lista de todas as ocorrências de "o" na string
print(var)
print(var2)


print(type(var)) #mostra o tipo do objeto var
print(type(var2)) #mostra o tipo do objeto var2



#Matéria aula:

import re as reg

# Padrões 
# "ABC"   -----------> procura o padrão ABC no texto
# [A-L]   -----------> procura o padrão A a L no texto
#  *.mp3

#funções

#reg.search()   ------ procura em qualquer parte do texto
#reg.match()    ------ procura no inicio da string
#reg.findall()  ------ devolve todas as ocurrencias na string
#reg.split()    ------ divide a string em partes por padrão

email= "sdasdas@gmail.com"
padrao=r"^[\w\.]+@[\w]+\.\w+$"

resultado=reg.match(padrao,email)

print (resultado)
print (resultado.group())
print (resultado.start())
print (resultado.end())
print (resultado.span())

#[] lista
#{
# nome: Pedro
# } dicionario /objeto

#https://regex101.com/
#https://overthewire.org/wargames/