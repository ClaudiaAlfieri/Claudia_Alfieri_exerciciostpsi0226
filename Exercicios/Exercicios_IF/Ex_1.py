
# Desenvolva um programa que assuma uma entrada em segundos e a converta para horas, minutos e segundos.

seg=int(input("Insira um número em segundos: "))

horas = seg // 3600
resto = seg % 3600
minutos = resto // 60
segundos = resto % 60

print(horas, "hora(s),", minutos, "minuto(s) e", segundos, "segundo(s)")

