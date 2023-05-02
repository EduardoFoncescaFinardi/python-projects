salarios = []
soma = 0

for i in range(4):
    salario = float(input('Salário: '))
    soma += salario
    salarios.append(salario)

media = soma / 4
print("média:", media)
for salario in salarios:
    if salario < media:
        print(f'Abaixo da média: R$ {salario}')