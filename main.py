# Importa o módulo onde estão as funções de manipulação de tarefas (adicionar, listar, remover)
import task

# Define a função principal que exibe o menu e gerencia as escolhas do usuário
def menu():

    # Loop infinito para manter o menu funcionando até que o usuário escolha sair
    while True:

        # Exibe o menu com as opções
        print("\nEntarefado: para você que está atolado de trabalho ter uma vida mais organizada!")
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefa")
        print("3. Remover Tarefa")
        print("4. Sair")

        # Tenta converter a entrada do usuário para número (int)
        try:
            choose = int(input("Escolha uma opção: "))
        except ValueError:
            # Caso o usuário digite algo que não seja número
            print("Por favor, digite um número válido.")
    
        # Se a escolha for 1, adiciona uma nova tarefa
        if choose == 1:
            taskName = input("Digite o nome da tarefa: ")
            task.addTask(taskName)

        # Se a escolha for 2, lista as tarefas existentes
        elif choose == 2:
            task.listTask()
        
        # Se a escolha for 3, lista as tarefas e remove uma com base no número informado
        elif choose == 3:
            task.listTask() # Mostra tarefas antes de remover
            try:
                number = int(input("Informe o número da tarefa para removê-la: "))
                task.removeTask(number)
            except ValueError:
                print("Número inválido. Tarefa não encontrada.")

        # Se a escolha for 4, finaliza o programa
        elif choose == 4:
            print("Até mais!")
            break # Sai do loop infinito e encerra o programa
        
        # Se o número for diferente das opções válidas
        else:
            print("Inválido! Tente novamente.")

menu()