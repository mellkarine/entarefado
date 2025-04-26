# Cria uma lista vazia para armazenar as tarefas
tasks = []

# Função que adiciona uma tarefa à lista
def addTask(task):
    tasks.append(task)

def listTask():

    # Se a lista estiver vazia
    if not tasks:
        print("Não há nenhuma tarefa aqui! Pode procrastinar!")
    
    # Se houver tarefas na lista
    else:
        print("Tarefas do entarefado:")
        for i, task in enumerate(tasks, start = 1):
            print(f"{i}. {task}")

# Função que remove uma tarefa com base no número informado
def removeTask(number):

    if 1 <= number <= len(tasks): # Verifica se o número é válido (dentro dos índices da lista)
        removed = tasks.pop(number - 1) # Remove a tarefa correspondente
        print(f"Tarefa '{removed}' removida com sucesso! Se livrou, entarefadinho.")

    else:
        print("Tarefa não encontrada. Tente novamente, entarefado!")

addTask("Estudar Python")
addTask("Fazer exercícios")
listTask()
removeTask(1)
listTask()