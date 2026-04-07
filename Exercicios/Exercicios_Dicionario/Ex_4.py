# Exercício 4: Verificar se uma chave existe
# Dado o dicionário:
# utilizador = {'nome': 'Carlos', 'idade': 28}
# Escreve um código que verifique se a chave email está presente no dicionário e imprima uma mensagem adequada, por exemplo: "Email não encontrado."

utilizador = {'nome': 'Carlos', 'idade': 28}

def verificar_chave(dicionario, chave):
    if chave in dicionario:
        print(f"{chave} encontrado.")
    else:
        print(f"{chave} não encontrado.")

verificar_chave(utilizador, "email")