from chatbot import entarefado

# Execução do programa
if __name__ == "__main__":  # Garante que o código abaixo seja executado apenas quando este script for executado diretamente
    while True:
        print("Iniciando o Entarefado 2.0... 🤖")  # Exibe uma mensagem de boas-vindas
        entarefado()  # Chama a função do chatbot para iniciar a interação

        # Pergunta ao usuário se ele deseja iniciar novamente o chatbot
        resposta = input("Gostaria de iniciar novamente? (sim/não): ").lower()  # Lê a resposta do usuário

        if resposta != "sim":  # Se a resposta não for "sim", o programa sai
            print("Entarefado 2.0 encerrado! Foi um prazer ajudar você 🤖")  # Mensagem de despedida
            break  # Encerra o loop