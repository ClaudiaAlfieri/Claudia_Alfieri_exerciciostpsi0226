
#Crie um algoritmo que mostre os 10 primeiros números primos. 
   
   
contagem = 0   
numero = 2   

while contagem < 10:       
    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False

    if primo:
        print(numero)
        contagem = contagem + 1  
        
    numero = numero + 1          