
#Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
# 1, 1, 2, 3, 5, 8, 13, 21.
# Como se constrói.
# 1+1=2
#     1+2=3
#         2+3=5

a = 1
b = 1

print(a)
print(b)

for i in range(60):
    c = a + b
    print(c)

    a = b
    b = c
