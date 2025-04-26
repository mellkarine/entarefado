# Importação das funções do módulo manager
import sys  # Para manipulação de saída no terminal
import time  # Para adicionar atrasos de tempo
from manager import addTask, listTask, concludeTask, deleteTask  # Importando as funções do módulo manager para gerenciar as tarefas

# Função de ajuda que mostra os comandos disponíveis para o usuário
def help():
    # Exibe a lista de comandos disponíveis para o usuário interagir com o chatbot
    print("\n📚 Comandos disponíveis:")
    print("  1. adicionar - Adiciona uma nova tarefa")  # Explica o comando para adicionar uma tarefa
    print("  2. listar    - Lista todas as tarefas")     # Explica o comando para listar tarefas
    print("  3. concluir  - Conclui uma tarefa")         # Explica o comando para concluir uma tarefa
    print("  4. apagar    - Apaga uma tarefa")          # Explica o comando para apagar uma tarefa
    print("  5. ajuda     - Mostra os comandos disponíveis")  # Explica o comando para mostrar a ajuda
    print("  6. sair      - Encerra o programa")        # Explica o comando para sair do programa

# Função que simula uma animação de carregamento com pontos
def animar(msg, pontos = 3, delay = 0.5):
    # Exibe a mensagem inicial
    print(msg, end = '')
    
    # Adiciona uma sequência de pontos para simular carregamento
    for _ in range(pontos):
        print('.', end = '')
        sys.stdout.flush()  # Força a impressão imediata no terminal
        time.sleep(delay)   # Atraso entre os pontos
    print()  # Nova linha após a animação

# Função principal do chatbot que interage com o usuário
def entarefado():
    # Exibe a saudação inicial e os comandos disponíveis
    print("Olá! Eu sou o Entarefado 2.0 🤖. Como posso te ajudar hoje?")
    help()  # Chama a função help() para exibir os comandos
    
    while True:  # Loop infinito que mantém o chatbot ativo até o usuário decidir sair
        command = input("> ").lower().strip()  # Lê o comando do usuário e converte para minúsculas

        # Comando para adicionar tarefa
        if command == "1" or command == "adicionar":
            task = input("Qual o nome da nova tarefa? ")  # Pergunta o nome da nova tarefa
            animar("Adicionando tarefa 🤖")  # Exibe a animação de carregamento
            addTask(task)  # Chama a função addTask do módulo manager para adicionar a tarefa
            print(f"Tudo certo! A tarefa '{task}' foi adicionada ao seu radar de afazeres! 🚀")  # Mensagem de confirmação

        # Comando para listar todas as tarefas
        elif command == "2" or command == "listar":
            animar("Carregando sua lista de tarefas 🤖")  # Exibe a animação de carregamento
            tasks = listTask()  # Chama a função listTask do módulo manager para obter todas as tarefas

            # Se houver tarefas, exibe a lista
            if tasks:
                print("🗒️ Suas tarefas:")
                for idx, task in enumerate(tasks):  # Itera sobre as tarefas e imprime com o índice
                    print(f"{idx + 1}. {task.strip()}")  # Exibe a tarefa com numeração (índice + 1)
            else:  # Se não houver tarefas
                print("🚫 Você ainda não tem tarefas.")

        # Comando para concluir uma tarefa
        elif command == "3" or command == "concluir":
            try:
                # Pergunta o número da tarefa que o usuário quer concluir
                indice = int(input("✅ Qual número da tarefa você quer concluir? ")) - 1
                animar("Concluindo tarefa 🤖")  # Exibe a animação de carregamento
                concludeTask(indice)  # Chama a função concludeTask para concluir a tarefa
                print("🎯 Tarefa finalizada! 🎉 Mais uma vitória no seu dia! Vamos para a próxima!")  # Mensagem de sucesso

            except ValueError:  # Caso o usuário insira um número inválido
                print("❗ Número inválido! Tente novamente.")  # Exibe mensagem de erro

        # Comando para apagar uma tarefa
        elif command == "4" or command == "apagar":
            try:
                # Pergunta o número da tarefa que o usuário quer apagar
                indice = int(input("🗑️ Qual o número da tarefa que você quer apagar?")) - 1
                animar("Apagando tarefa 🤖")  # Exibe a animação de carregamento
                deleteTask(indice)  # Chama a função deleteTask para apagar a tarefa
                print("🧹 Prontinho! Sua tarefa foi eliminada do radar.")  # Mensagem de confirmação

            except ValueError:  # Caso o usuário insira um número inválido
                print("❗ Número inválido! Tente novamente.")  # Exibe mensagem de erro

        # Comando para mostrar os comandos disponíveis
        elif command == "5" or command == "ajuda":
            animar("Consultando comandos disponíveis 🤖")  # Exibe a animação de carregamento
            help()  # Chama a função help() para exibir os comandos

        # Comando para sair do chatbot
        elif command == "6" or command == "sair":
            animar("Encerrando o Entarefado 🤖")  # Exibe a animação de encerramento
            print("Até logo! 👋")  # Mensagem de despedida
            break  # Encerra o loop do chatbot, encerrando o programa

    time.sleep(1)  # Pausa o programa por 1 segundos antes de encerrar (opcional)