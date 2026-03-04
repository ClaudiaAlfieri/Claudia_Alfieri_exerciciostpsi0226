
# Analisa um valor e retorna o seu tipo:
# •	Número inteiro
# •	Número decimal
# •	String numérica
# •	String textual
# •	Lista
# •	Tipo desconhecido

val = input("Digite um valor: ")

if val.startswith("[") and val.endswith("]"):
    # verifica se tem []
    print("Lista")
elif val.isdigit():
    # verifica se são só números
    print("Número inteiro")
elif val.replace(".", "", 1).isdigit():
    # tira o .
    print("Número decimal")
elif val.replace(" ", "").isdigit(): 
    # tira os espaços
    print("String numérica")
elif val.isalpha():
    # verifica se só tem letras
    print("String textual")
else:
    print("Tipo desconhecido")