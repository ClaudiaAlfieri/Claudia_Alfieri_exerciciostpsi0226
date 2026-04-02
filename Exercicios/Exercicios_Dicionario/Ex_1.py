# Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
# 1-	Inserir
# 2-	Listar
# O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
# Exemplo:
# nome: Maria
# idade: 20
# curso: Engenharia

alunos = []

#1 - inserir aluno
def insert(alunos: list):
    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")
    alunos.append({"Nome": nome, "Idade": idade, "Curso": curso})

#2 - listar alunos
def listar(alunos: list):
    for aluno in alunos:
        print(f"Nome: {aluno['Nome']}")
        print(f"Idade: {aluno['Idade']}")
        print(f"Curso: {aluno['Curso']}")
        print("---")

while True:
    print("1 - inserir aluno")
    print("2 - listar alunos")
    print("3 - sair")
    opt = input("Escolha Opção: ")
    match opt:
        case "1":
            insert(alunos)
        case "2":
            listar(alunos)
        case "3":
            print("fim do programa")
            break
        case _:
            print("opção inválida")