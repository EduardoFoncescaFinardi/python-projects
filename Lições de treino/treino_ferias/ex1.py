#Sistema de Gerenciamneto de Tarefas

#part 1: functionality that alllows the user to add tasks

def task_add(): 
  print("Want to add how many tasks?")
  tasks_amount = int(input("number os tasks:"))
  task_list = []
  for i in range(tasks_amount):
    task = input("Describre task: ")
    task_list.append(task)
    i += 1
  print(task_list)

#part 2: 

def main():
  task_add()

main()