import json
from datetime import datetime

# Função que lê as tarefas do arquivo 'tasks.json'
def upTask():
    
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)  # Carrega o conteúdo do JSON
    except FileNotFoundError:
        # Se o arquivo não existir, cria um dicionário vazio
        tasks = {}
    return tasks  # Retorna o dicionário de tarefas

# Função para salvar as tarefas no arquivo 'tasks.json'
def saveTask(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)  # Salva as tarefas no arquivo JSON, com indentação

# Função para adicionar uma nova tarefa
def addTask(titulo, descricao, prioridade, prazo):
    tasks = upTask()  # Carrega as tarefas existentes
    task_id = str(len(tasks) + 1)  # Gera um novo ID como string
    criado_em = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Hora atual como string formatada
    tasks[task_id] = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "prazo": prazo,
        "status": "Em andamento",
        "criado_em": criado_em
    }
    saveTask(tasks)  # Salva o dicionário atualizado no JSON

# Função para listar todas as tarefas
def listTask():
    tasks = upTask()  # Chama a função upTask para pegar todas as tarefas
    return tasks  # Retorna o dicionário de tarefas

# Função para concluir uma tarefa
def concludeTask(task_id):
    tasks = upTask()  # Pega todas as tarefas
    if task_id in tasks:  # Verifica se a tarefa existe
        tasks[task_id]['status'] = 'Concluída'  # Atualiza o status
        saveTask(tasks)  # Salva no JSON

# Função para excluir uma tarefa com base no índice fornecido
def deleteTask(task_id):
    tasks = upTask()  # Pega todas as tarefas
    if task_id in tasks:  # Verifica se a tarefa existe
        del tasks[task_id]  # Deleta a tarefa pelo ID
        saveTask(tasks)  # Salva no JSON