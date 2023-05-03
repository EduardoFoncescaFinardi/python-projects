numeros = []

for i in range(5):
    numero = int(input("N:"))
    numeros.append(numero)

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    
print("O maior número é:", maior)


    

