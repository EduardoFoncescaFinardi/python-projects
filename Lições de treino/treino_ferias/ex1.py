#Sistema de Gerenciamneto de Tarefas

#parte 1: functionality that alllows the user to add tasks

def task_add(): 
  print("Want to add how many tasks?")
  tasks_amount = int(input("number os tasks:"))
  task_list = []
  for i in range(tasks_amount):
    task_list.append(listadepecas[opcao - 1])