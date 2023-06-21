#Sistema de Gerenciamneto de Tarefas

#part 1: functionality that alllows the user to add tasks

def task_add(): 
  print("Want to add how many tasks?")
  tasks_amount = int(input("number os tasks:"))
  task_list = []
  for i in  range(tasks_amount):
    task = input("Describre task: ")
    task_list.append(task)
    i += 1

  return task_list
#part 2: functionality that alllows the user to edit tasks

def task_edit(task_list):
  print("Do you want to edit any task?")
  confirmation = int(input("""1 - Yes 
2 - No?
"""))
  
  match confirmation: 
    case 1:
      print(task_list)
      which_task = int(input("Which one?: "))
    
    case 2:
      print


def main():
  task_list = task_add()
  task_edit(task_list)

main()