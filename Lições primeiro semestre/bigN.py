n = int(input('Número: '))
maior = 0

while n != 0:
    if n > maior:
        maior = n
        n = int(input('Número: '))
    else:
        maior = n
        n = int(input('Número: '))

print(f'Maior: {maior}')