# Métodos são comportamentos de um objeto
# Funções são blocos de código que realizam uma tarefa específica e podem ser reutilizados em diferentes partes do programa.

# Funções:
# É um bloco de código que pode ser chamado repetidamente evitando a repetição do código.
# Dado pertencer a um bloco de código pequeno, torna-se mais fácil a manutenção.
# Em segurança no scope quando bem aplicada uma função.

# Scopes e manipulação são feitos através de passagem de valores/parametros e passagem das referências das variáveis.

num1=12
num2=13
 
# Estrutura da função:
# Valor_de_retorno nome_da_função (parametros_de_entrada)


#Na maioria das linguagens de programação, a troca de valores entre duas variáveis é feita usando uma variável temporária para armazenar um dos valores durante a troca. 
    # troca = 0
    # troca = num1
    # num1 = num2
    # num2 = troca    
    #No entanto, em Python, podemos realizar a troca de valores de forma mais simples e direta usando a atribuição múltipla.
    
# Passagem por valor normal:

def troca(nu1, nu2):        
    nu1, nu2 = nu2, nu1
    print("Antes da troca - num 1: ",nu1,", num 2: ",nu2)
    return nu1, nu2
  
num1, num2 =troca(num1,num2)
  
print("num 1: ",num1,", num 2: ",num2)

# Passagem por referência de memória:

lista1 = [12, 13, 14]

def insertValue(lista):
    lista.append(19)
    
    insertValue(lista1)
    print("Lista depois da função ",lista1)
    