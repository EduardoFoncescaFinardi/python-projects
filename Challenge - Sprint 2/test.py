listadepecas = ["Quadro", "Guidão", "Manoplas", "Manete de Freio", "Alavanca de Câmbio", "Mesa",
                "Headset ou Caixa de Direção", "Garfo", "Rodas", "Freio", "Câmbio Dianteiro",
                "Câmbio Traseiro", "Cassete", "Corrente", "Movimento Central", "Pedivela", "Pedal",
                "Selim", "Canote de Selim", "Abraçadeira de Selim", "Suspensão Traseira"]

qntpecas = int(input("Quantidade de peças danificadas: "))

while qntpecas < 0 or qntpecas > len(listadepecas):
    print("Quantidade inválida! Máximo de 21 peças!")
    qntpecas = int(input("Quantidade de peças danificadas: "))

quaispecas = []
print("------------------------------------------------------")
print("Certo! Agora declare qual(is) peça(s) foi danificada:")

for i in range(qntpecas):

    opcao = int(input("Peça(s): "))
    while opcao < 1 or opcao > len(listadepecas):
        print("Opção inválida! Escolha um número válido.")
        opcao = int(input("Peça(s): "))

    quaispecas.append(listadepecas[opcao - 1])

print("As peças danificadas são:", quaispecas)