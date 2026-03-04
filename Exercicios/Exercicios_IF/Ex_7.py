
#  O sistema de avaliação de uma disciplina tem três provas com pesos diferentes. A primeira tem peso 2, a segunda tem peso 3, e a terceira tem peso 5. Crie um programa para calcular a média final de um aluno e mostrar se ele está APROVADO (nota >= 6) ou REPROVADO (nota < 6).

nota1=float(input("Qual é o valor da nota 1?"))
nota2=float(input("Qual é o valor da nota 2?"))
nota3=float(input("Qual é o valor da nota 3?"))

media = (nota1*2 + nota2*3 + nota3*5) / (2+3+5)

if media >= 6:
    print(f"Média: {media} Aprovado")   
else:
    print(f"Média: {media} Reprovado")
