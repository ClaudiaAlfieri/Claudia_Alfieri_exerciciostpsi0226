# Cria um programa que criptografe e descriptografe mensagens utilizando a tabela ASCII e uma chave String. A chave será uma palavra ou frase fornecida pelo utilizador, e a criptografia será feita com base na soma dos valores ASCII dos caracteres dessa chave.
# Funcionamento da Criptografia
# 1.	O utilizador introduz:
# o	Uma mensagem (ex: "Olá Mundo")
# o	Uma chave em formato de string (ex: "chave")
# 2.	O programa:
# o	Calcula a chave numérica, somando os valores ASCII de cada letra da chave:
# 	"chave" → 'c'=99, 'h'=104, 'a'=97, 'v'=118, 'e'=101
# Soma: 99 + 104 + 97 + 118 + 101 = **519**
# o	Usa essa soma (519) como valor para criptografar cada caractere da mensagem:
# 	'O' → ord('O') = 79 → 79 + 519 = 598
# 	'l' → ord('l') = 108 → 108 + 519 = 627
# 	etc.
# 3.	Para descriptografar, o programa deve subtrair o mesmo valor (519 neste caso) de cada número para recuperar os caracteres originais.
# Requisitos:
# 1.	O programa deve conter três funções:
# o	criptografar(mensagem: str, chave: str) -> List[int]
# o	descriptografar(codigos: List[int], chave: str) -> str
# o	Listar
# 2.	Utilizar apenas funções nativas (ord() e chr()).
# 3.	Manter os espaços, acentos e distinguir entre maiúsculas e minúsculas.
# 4.	Impede que a chave seja vazia.
# 5.	Aplica rotação aos caracteres da mensagem encriptada (entre ASCII 32 e 126), para mantê-los dentro deste intervalo.


def calcular_chave(chave: str) -> int:
    # Soma os valores ASCII de cada caractere da chave
    soma = 0
    for letra in chave:
        soma += ord(letra)
    return soma

def criptografar(mensagem: str, chave: str) -> list:
    valor_chave = calcular_chave(chave)
    codigos = []
    
    for caractere in mensagem:
        codigo = ord(caractere) + valor_chave
        # Rotação: mantém o código entre ASCII 32 e 126
        codigo = 32 + (codigo - 32) % 95
        codigos.append(codigo)
    
    return codigos

def descriptografar(codigos: list, chave: str) -> str:
    valor_chave = calcular_chave(chave)
    mensagem = ""
    
    for codigo in codigos:
        # Desfaz a rotação e subtrai a chave
        original = 32 + (codigo - 32 - valor_chave % 95) % 95
        mensagem += chr(original)
    
    return mensagem

def listar(codigos: list):
    print("Códigos criptografados:", codigos)


# Pede a mensagem
mensagem = input("Escreve a mensagem: ")

# Pede a chave 
chave = input("Escreve a chave: ")
while chave == "":
    print("A chave não pode estar vazia!")
    chave = input("Escreve a chave: ")

# Criptografa
codigos = criptografar(mensagem, chave)

# Lista os códigos
listar(codigos)

# Descriptografa
mensagem_original = descriptografar(codigos, chave)
print("Mensagem descriptografada:", mensagem_original)
   