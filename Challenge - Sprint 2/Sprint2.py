def menu():
    selecao = int(input("""
*-- MENU --*

1 - realizar vistoria, em caso de acidente;
2 - realizar vistoria, em caso de renovação de seguro;
3 - realizar vistoria, em caso de assinar seguro; 

Selecionar item de acordo com necessidade: """))
    while selecao not in [1, 2, 3]:
        print("------------------------------------")
        print("Selecione apenas as opções de 1 a 3!")
        selecao = int(input("""
*-- MENU --*

1 - realizar vistoria, em caso de acidente;
2 - realizar vistoria, em caso de renovação de seguro;
3 - realizar vistoria, em caso de assinar seguro; 

Selecionar item de acordo com necessidade: """))
    return selecao

def selecao_menu(selecao):
    if selecao == 1:
      print("------------------------------------------------------")
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
      print("""
Certo! Agora declare qual(is) peça(s) foi(foram) danificada:
      1 - Quadro
      2 - Guidão
      3 - Manoplas
      4 - Manete de Freio
      5 - Alavanca de Câmbio
      6 - Mesa
      7 - Headset ou Caixa de Direção
      8 - Garfo
      9 - Rodas
      10 - Freio
      11 - Câmbio Dianteiro
      12 - Câmbio Traseiro
      13 - Cassete
      14 - Corrente
      15 - Movimento Central
      16 - Pedivela
      17 - Pedal
      18 - Selim
      19 - Canote de Selim
      20 - Abraçadeira de Selim
      21 - Suspensão Traseira
        """)

      for i in range(qntpecas):

        opcao = int(input("Peça(s): "))
        while opcao < 1 or opcao > len(listadepecas):
          print("Opção inválida! Escolha um número válido.")
          opcao = int(input("Peça(s): "))

        quaispecas.append(listadepecas[opcao - 1])

      print("As peças danificadas são:", quaispecas, "Certo?")
      question = input("(S)im ou (N)ão:")
      while question != "S" and question != "N":
        print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
        question = input("(S)im ou (N)ão:")
      
      print("------------------------------------------------------")

      print("""Obrigado por se utilizar de nossos serviços!
O encaminharemos para o setor de upload de fotos
para darmos sequência a vistoria!""")

      
      
    

    
    elif selecao == 2:
      print("------------------------------------------------------------")
      print("Certo! nos envie os dados, com as marcas gerais da bicicleta")
      qntmarcas = int(input("quantidade de peças com marcas distintas: "))
      list = []
      i = 0
      while i < qntmarcas:
          marcas = input("Marcas: ")
          list.append(marcas)
          i += 1
      
      
        
      print("As marcas que compõe sua bicicleta, são", list , "Correto?")
      question = input("(S)im ou (N)ão:")
      while question != "S" and question != "N":
        print("Opção inválida! Apenas 'S' para sim e 'N' para não!")
        question = input("(S)im ou (N)ão:")
    
    else:
      print("------------------------------------------------------------")
      print("Certo! Você será encaminhado para a sessão de cadastro, para dar sequência e enviar os dados da bicicleta!")


def main():
    selecao = menu()
    selecao_menu(selecao)

main()
        

       
            

        

          
          