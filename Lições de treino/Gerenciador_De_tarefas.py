#Projeto 1: Gerenciador de Tarefas (To-Do List)
# Descrição
# Crie um gerenciador de tarefas simples onde o usuário pode adicionar, remover e visualizar tarefas. Utilize listas para armazenar as tarefas e dicionários para armazenar detalhes adicionais sobre cada tarefa.

# Funcionalidades
# Adicionar uma nova tarefa
# Remover uma tarefa existente
# Marcar uma tarefa como concluída
# Exibir todas as tarefas
# Exibir apenas as tarefas concluídas ou pendentes
# Estruturas Utilizadas
# Listas para armazenar as tarefas
# Dicionários para armazenar detalhes das tarefas (ex.: descrição, status)

def adicionar_tarefa(tarefas, descricao):
  tarefa = {'descricao': descricao, 'status': False}
  tarefas.append(tarefa)
  return tarefa



def remover_tarefa(tarefas, indice_tarefa):
  if 0 <= indice_tarefa < len(tarefas):
    tarefas.pop(indice_tarefa)
        
        

def visualizar_tarefa(tarefas, tarefa):
  visu_quest = int(input("""Gostaria de visualizar status de alguma tarefa?
1. Sim
2. Não
Resposta: """))
  if visu_quest == 1:
    print("Lista de Tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"{i}. {tarefa['descricao']} - {'Concluída' if tarefa['status'] else 'Pendente'}")
  else:
    return
  
  
def atualizar_tarefa(tarefas, indice_tarefa):
  if 0 <= indice_tarefa < len(tarefas):
    tarefas[indice_tarefa]['status'] = True
    print(f"Status da tarefa '{tarefas[indice_tarefa]['descricao']}' alterado para {'Concluída' if True else 'Pendente'}.")
  else:
    print("Índice inválido.")

def main():
  tarefas = []
  y = True
  while y:
    menu = int(input("""
1. Adicionar Tarefa
2. Remover Tarefa
3. Visualizar Tarefas
4. alterar status de uma tarefa
Resposta: """))
    match menu:
      case 1:
        descricao = input("Descrição da Tarefa: ")
        tarefa = adicionar_tarefa(tarefas, descricao)
      case 2:
        print(tarefas)
        print("Escolha uma tarefa para ser removida")
        indice_tarefa = int(input("Número da tarefa: "))
        remover_tarefa(indice_tarefa, tarefas)
      case 3:
        visualizar_tarefa(tarefas, tarefa)
      case 4:
        print("Escolha uma tarefa para ser removida")
        indice_tarefa = int(input("Número da tarefa: "))
        atualizar_tarefa(tarefas, indice_tarefa)
    x = True
    while x:
      verificação = int(input("""Gostaria de continuar manipulando as tarefas?
1 - Sim
2 - Não
Resposta:"""))
      
      if verificação == 1:
        y = True
        x = False
        
      elif verificação == 2:
        x = False
        y = False
        
      else: 
        print("Coloque uma resposta válida!")
  
  

main()