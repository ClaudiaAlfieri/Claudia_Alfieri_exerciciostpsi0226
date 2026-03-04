
# Crie um programa que leia a nota de 10 alunos (notas de 0 a 20), calcule a média das notas e mostre a média. Além disso, informe quantos alunos ficaram com a nota igual ou acima da média. 

nota1=float(input("Qual é o valor da nota do aluno 1?"))
nota2=float(input("Qual é o valor da nota do aluno 2?"))
nota3=float(input("Qual é o valor da nota do aluno 3?"))
nota4=float(input("Qual é o valor da nota do aluno 4?"))
nota5=float(input("Qual é o valor da nota do aluno 5?"))
nota6=float(input("Qual é o valor da nota do aluno 6?"))
nota7=float(input("Qual é o valor da nota do aluno 7?"))
nota8=float(input("Qual é o valor da nota do aluno 8?"))
nota9=float(input("Qual é o valor da nota do aluno 9?"))
nota10=float(input("Qual é o valor da nota do aluno 10?"))

media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10)/10

alunos_acima = 0

if nota1  >= media: alunos_acima += 1
if nota2  >= media: alunos_acima += 1
if nota3  >= media: alunos_acima += 1
if nota4  >= media: alunos_acima += 1
if nota5  >= media: alunos_acima += 1
if nota6  >= media: alunos_acima += 1
if nota7  >= media: alunos_acima += 1
if nota8  >= media: alunos_acima += 1
if nota9  >= media: alunos_acima += 1
if nota10 >= media: alunos_acima += 1
    


print(f"A média das notas da turma é {media} e o número de alunos com nota acima da média foi {alunos_acima}")