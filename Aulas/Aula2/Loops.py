#Loops For // While
#[] = array ou lista em qq lingugem de programação


nomes = ["Joao", "Pedro", "Antonio"]
#index      0       1        2

for nome in nomes:
    print(nome)
    
# Função range
  
for i in range(3):
    print(nomes[i])

for i in range(1,11):
    print(i)
    #range(1,11) gera uma sequência de números de 1 a 10, o número 11 é exclusivo, ou seja, não é incluído na sequência gerada.
    
for i in range(1,20,2):
    print(i)
    
#range(1,20,2) gera uma sequência de números de 1 a 19, com um passo de 2, ou seja, inclui apenas os números ímpares dentro desse intervalo. O número 20 é exclusivo, ou seja, não é incluído na sequência gerada.
    
    
#While = controlado por uma expressão, ex: val 1< val2

#tamanho da lista 3

ifinal = len(nomes)
i=0
while i < ifinal: #começa em 0 e acaba em 2.
    print(nomes[i])
    i+=1
    
    
ifinal = len(nomes)
i=0
while i < ifinal: #começa em 0 e acaba em 2.
    print("Controlo de iterador", i)
    print(nomes[i])
    i+=2 #pula de 2 em 2
