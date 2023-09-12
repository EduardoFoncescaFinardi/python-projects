import json

quadro = ["Quadro", "Pedal", "Pedivela", "Caixa de direção", "Garfo"]
guidao = ["Guidão", "Manoplas", "Manete de Freio", "Alavanca de Freio"]
selim = ["Selim", "Canote", "Mesa", "Abraçadeira"]
rodas = ["Rodas", "Freio", "Câmbio Traseiro", 'Câmbio Dianteiro', "Cassete", "Corrente", "Suspensão Traseira"]

print("""Certo! Agora começará uma série de perguntas relacionadas 
a cada parte da sua bicicleta para você declarar cada peça.""")
print("---------------------------------------------------------------")
responseData = {
    "Quadro": [],
    "Guidão": [],
    "Selim": [],
    "Rodas": [],
}

for i in range(0,4):

  match i:
    case 0: 
      i = 0
      for item in quadro:
        print(f'Item de decleração, {item};')
        nome_da_peça = input("Nome da peça:")
        responseData["Quadro"].append(nome_da_peça)
        print("-----------------------------")
  
    case 1:
      for item in guidao:
        print(f'Item de decleração, {item};')
        nome_da_peça = input("Nome da peça:")
        responseData["Guidão"].append(nome_da_peça)
        print("-----------------------------")

    case 2: 
      for item in selim:
        print(f'Item de decleração, {item};')
        nome_da_peça = input("Nome da peça:")
        responseData["Selim"].append(nome_da_peça)
        print("-----------------------------")

    case 3:
      for item in rodas:
        print(f'Item de decleração, {item};')
        nome_da_peça = input("Nome da peça:")
        responseData["Rodas"].append(nome_da_peça)
        print("-----------------------------")
  i += 1