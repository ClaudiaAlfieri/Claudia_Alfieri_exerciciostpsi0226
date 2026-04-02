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










# LOOPS EM PYTHON
# Existem vários tipos de ciclos (loops) para repetir código:
# - for (foreach) → percorre listas ou sequências
# - while → repete enquanto uma condição for verdadeira

# -----------------------------------------------------
# LISTA (ARRAY)
# Uma lista guarda vários valores na mesma variável

nomes = ["Joao", "Pedro", "Antonio"]

# índices da lista
# posição: 0       1        2
# valor :  Joao   Pedro   Antonio


# -----------------------------------------------------
# LOOP FOR (FOREACH)

# Percorre diretamente os elementos da lista
for nome in nomes:
    print(nome)

# Neste caso a variável "nome" recebe cada elemento da lista


# -----------------------------------------------------
# FUNÇÃO range()

# range() cria uma sequência de números

# range(len(nomes)) → cria números de 0 até ao tamanho da lista - 1
for i in range(len(nomes)):
    print(nomes[i])

# Aqui usamos o índice para aceder aos elementos da lista


# range(1,11) → gera números de 1 até 10
for i in range(1, 11):
    print(i)


# -----------------------------------------------------
# LOOP WHILE
# O while executa enquanto uma condição for verdadeira

ifinal = len(nomes)  # tamanho da lista

# tamanho da lista = 3
i = 0

while i < ifinal:  # começa em 0 e termina em 2
    print("controlo de iterador:", i)
    print(nomes[i])

    i += 1  # incrementa o contador


# -----------------------------------------------------
# LOOP INFINITO COM MENU

# while True cria um ciclo infinito
# normalmente usado em menus de programas

while True:

    print("1 - Bom dia")
    print("2 - Boa tarde")
    print("3 - Sair")

    opc = input("Introduza uma opção: ")

    # match funciona como switch-case (outras linguagens)
    match opc:

        case "1":
            print("Bom dia")

        case "2":
            print("Boa tarde")

        case "3":
            print("Sair do programa")
            break  # termina o ciclo

        case _:
            print("Opção inválida")