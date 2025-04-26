# Função que lê as tarefas do arquivo 'tasks.txt'
def upTask():
    tasks = []  # Inicializa uma lista vazia para armazenar as tarefas
    try:
        # Abre o arquivo 'tasks.txt' para leitura ('r') e lê as linhas
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()  # Lê todas as linhas do arquivo e armazena na lista 'tasks'
    except FileNotFoundError:
        # Se o arquivo não for encontrado, não faz nada (simplesmente continua sem carregar tarefas)
        pass
    return tasks  # Retorna a lista de tarefas (vazia ou com as tarefas do arquivo)

# Função para salvar as tarefas no arquivo 'tasks.txt'
def saveTask(tasks):
    # Abre o arquivo 'tasks.txt' para escrita ('w') e escreve as tarefas
    with open('tasks.txt', 'w') as f:
        f.writelines(tasks)  # Escreve todas as tarefas na lista 'tasks' no arquivo

# Função para adicionar uma nova tarefa
def addTask(task):
    tasks = upTask()  # Chama a função upTask para pegar as tarefas atuais
    tasks.append(f'{task} [Em andamento]\n')  # Adiciona a nova tarefa à lista com o status 'Em andamento'
    saveTask(tasks)  # Chama a função saveTask para salvar a lista de tarefas atualizada no arquivo

# Função para listar todas as tarefas
def listTask():
    tasks = upTask()  # Chama a função upTask para pegar todas as tarefas
    return tasks  # Retorna a lista de tarefas (em formato de texto)

# Função para concluir uma tarefa, com base no índice fornecido
def concludeTask(indice):
    tasks = upTask()  # Chama a função upTask para pegar todas as tarefas
    if 0 <= indice < len(tasks):  # Verifica se o índice é válido (se a tarefa existe na lista)
        task = tasks[indice]  # Pega a tarefa no índice fornecido
        tasks[indice] = task.replace('[Em andamento]', '[Concluída]')  # Substitui o status da tarefa para 'Concluída'
        saveTask(tasks)  # Salva a lista de tarefas com o status atualizado no arquivo

# Função para excluir uma tarefa com base no índice fornecido
def deleteTask(indice):
    tasks = upTask()  # Chama a função upTask para pegar todas as tarefas
    if 0 <= indice < len(tasks):  # Verifica se o índice é válido (se a tarefa existe na lista)
        del tasks[indice]  # Remove a tarefa no índice fornecido
        saveTask(tasks)  # Salva a lista de tarefas atualizada no arquivo, sem a tarefa excluída