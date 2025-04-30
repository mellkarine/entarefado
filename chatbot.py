import sys
import time
from datetime import datetime
import json  # Importando o módulo json para manipulação de arquivos JSON
from manager import addTask, listTask, concludeTask, deleteTask  # Importando funções do módulo manager

# Função de ajuda que mostra os comandos disponíveis para o usuário
def help():
    print("\n📚 Comandos disponíveis:")
    print("  1. adicionar - Adiciona uma nova tarefa")
    print("  2. listar    - Lista todas as tarefas")
    print("  3. concluir  - Conclui uma tarefa")
    print("  4. apagar    - Apaga uma tarefa")
    print("  5. ajuda     - Mostra os comandos disponíveis")
    print("  6. sair      - Encerra o programa")

# Função que simula uma animação de carregamento com pontos
def animar(msg, pontos = 3, delay = 0.5):
    print(msg, end = '')
    for _ in range(pontos):
        print('.', end = '')
        sys.stdout.flush()  # Força a impressão imediata no terminal
        time.sleep(delay)   # Atraso entre os pontos
    print()

# Função para ler o arquivo JSON contendo as tarefas
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)  # Carrega as tarefas de um arquivo JSON
    except (FileNotFoundError, json.JSONDecodeError):  # Se o arquivo não existir ou estiver vazio
        tasks = {}  # Cria um dicionário vazio caso não haja tarefas
    return tasks

# Função para salvar as tarefas no arquivo JSON
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)  # Salva as tarefas no arquivo JSON com uma boa formatação

# Função principal do chatbot
def entarefado():
    print("Olá! Eu sou o Entarefado 2.0 🤖. Como posso te ajudar hoje?")
    help()  # Exibe os comandos
    while True:
        command = input("> ").lower().strip()  # Lê o comando do usuário e converte para minúsculas

        # Comando para adicionar tarefa
        if command == "1" or command == "adicionar":
            titulo = input("📌 Qual o título da tarefa? ").strip()
            descricao = input("📝 Descreva a tarefa: ").strip()
            prioridade = input("⚡ Qual a prioridade (baixa, média, alta)? ").strip().capitalize()
            prazo = input("📅 Qual o prazo (ex: 2025-05-15)? ").strip()
            data_criacao = datetime.now().strftime("%Y-%m-%d")

            animar("Adicionando tarefa 🤖")
            tasks = load_tasks()
            task_id = str(len(tasks) + 1)
            tasks[task_id] = {
                "titulo": titulo,
                "descricao": descricao,
                "prioridade": prioridade,
                "prazo": prazo,
                "data_criacao": data_criacao,
                "status": "Em andamento"
            }
            save_tasks(tasks)
            print(f"Tudo certo! A tarefa '{titulo}' foi adicionada com sucesso! 🚀")

        # Comando para listar todas as tarefas
        elif command == "2" or command == "listar":
            animar("Carregando sua lista de tarefas 🤖")
            tasks = load_tasks()

            if tasks:
                print("🗒️ Suas tarefas:")
                for task_id, data in tasks.items():
                    print(f"{task_id}. {data['titulo']} [{data['status']}]")
                    print(f"   📌 Prioridade: {data['prioridade']}")
                    print(f"   📅 Prazo: {data['prazo']} | Criada em: {data['data_criacao']}")
                    print(f"   📝 {data['descricao']}")
            else:
                print("🚫 Você ainda não tem tarefas.")

        # Comando para concluir uma tarefa
        elif command == "3" or command == "concluir":
            try:
                task_id = input("✅ Qual número da tarefa você quer concluir? ").strip()
                animar("Concluindo tarefa 🤖")
                tasks = load_tasks()  # Carrega as tarefas
                if task_id in tasks:  # Verifica se a tarefa existe
                    tasks[task_id]['status'] = 'Concluída'  # Atualiza o status da tarefa para 'Concluída'
                    save_tasks(tasks)  # Salva as alterações no arquivo JSON
                    print("🎯 Tarefa finalizada! 🎉 Mais uma vitória no seu dia! Vamos para a próxima!")
                else:
                    print("❗ Tarefa não encontrada!")

            except ValueError:
                print("❗ Número inválido! Tente novamente.")

        # Comando para apagar uma tarefa
        elif command == "4" or command == "apagar":
            try:
                task_id = input("🗑️ Qual o número da tarefa que você quer apagar? ").strip()
                animar("Apagando tarefa 🤖")
                tasks = load_tasks()  # Carrega as tarefas
                if task_id in tasks:  # Verifica se a tarefa existe
                    del tasks[task_id]  # Remove a tarefa do dicionário
                    save_tasks(tasks)  # Salva as alterações no arquivo JSON
                    print("🧹 Prontinho! Sua tarefa foi eliminada do radar.")
                else:
                    print("❗ Tarefa não encontrada!")

            except ValueError:
                print("❗ Número inválido! Tente novamente.")

        # Comando para mostrar os comandos disponíveis
        elif command == "5" or command == "ajuda":
            animar("Consultando comandos disponíveis 🤖")
            help()

        # Comando para sair do chatbot
        elif command == "6" or command == "sair":
            animar("Encerrando o Entarefado 🤖")
            print("Até logo! 👋")
            break

    time.sleep(1)  # Pausa antes de finalizar (opcional)