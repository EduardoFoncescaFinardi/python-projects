database = []

for i in range (3):
    x = input('Escolha a peça')
    y = input('Quer escolher a marca? Caso negativo, deixe em branco')
    database.append({
        "peça" : x,
        "marca" : y
    })

# primeira variavel é o índice numerico, segunda variavel é o proprio objeto - enumerate 
for index,jorge in enumerate(database):
    print(f"Item {index}: peça = {jorge['peça']} e marca = {jorge['marca']}")
