# Entarefado 2.0 🤖

**Entarefado 2.0** é um chatbot interativo desenvolvido para ajudar na organização das suas tarefas diárias. Através de uma interface simples de linha de comando, você pode gerenciar suas atividades, com funcionalidades como adicionar, listar, concluir e apagar tarefas, além de outras opções que tornam a interação eficiente e dinâmica.

## Funcionalidades

- **Adicionar Tarefas**: Permite adicionar novas tarefas ao seu radar de afazeres. Você pode definir um título, descrição, prioridade, prazo e visualizar a data de criação.
- **Listar Tarefas**: Exibe todas as tarefas que você adicionou, mostrando detalhes como título, status, prioridade, prazo e data de criação.
- **Concluir Tarefas**: Marca uma tarefa como concluída, permitindo o controle do que já foi realizado.
- **Apagar Tarefas**: Remove uma tarefa do seu radar de afazeres, mantendo seu gerenciamento de tarefas atualizado.
- **Comando de Ajuda**: Exibe os comandos disponíveis para facilitar a interação com o bot.
- **Encerrar o Programa**: Finaliza a execução do chatbot.

## Como Usar

1. Clone este repositório para o seu computador:

   ```bash
   git clone https://github.com/mellkarine/entarefado.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd entarefado
   ```

3. Execute o script principal:

   ```bash
   python main.py
   ```

4. Interaja com o bot! Ele irá apresentar uma lista de comandos que você pode usar para gerenciar suas tarefas.

## Comandos Disponíveis

- **adicionar** ou **1**: Adiciona uma nova tarefa. Você será solicitado a fornecer o título, descrição, prioridade, prazo e, automaticamente, a data de criação será registrada.
- **listar** ou **2**: Lista todas as tarefas. Exibe título, status, prioridade, prazo, data de criação e descrição das tarefas.
- **concluir** ou **3**: Conclui uma tarefa. Você pode selecionar o número da tarefa que deseja marcar como concluída.
- **apagar** ou **4**: Apaga uma tarefa. Você pode remover uma tarefa do seu radar de afazeres.
- **ajuda** ou **5**: Mostra os comandos disponíveis para facilitar a navegação no bot.
- **sair** ou **6**: Encerra o programa.

## Exemplo de Uso

```bash
Olá! Eu sou o Entarefado 2.0 🤖. Como posso te ajudar hoje?

📚 Comandos disponíveis:
  1. adicionar - Adiciona uma nova tarefa
  2. listar    - Lista todas as tarefas
  3. concluir  - Conclui uma tarefa
  4. apagar    - Apaga uma tarefa
  5. ajuda     - Mostra os comandos disponíveis
  6. sair      - Encerra o programa
> 1
Qual o nome da nova tarefa? Organizar a estante
Adicionando tarefa 🤖...
Tudo certo! A tarefa 'Organizar a estante' foi adicionada ao seu radar de afazeres! 🚀
```

## Tecnologias Utilizadas

- **Python**: Linguagem principal usada para desenvolver o chatbot.
- **sys**: Para manipulação de saída no terminal.
- **time**: Para adicionar delays e animações de carregamento.
- **datetime**: Para registrar e formatar as datas de criação e prazo das tarefas.
- **JSON**: Armazenamento das tarefas em formato JSON, garantindo a persistência e a leitura rápida.
- **Estrutura Modular**: O projeto é estruturado em módulos, com a lógica de gerenciamento de tarefas sendo encapsulada no módulo `manager.py`.

## Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma branch para sua nova funcionalidade:

   ```bash
   git checkout -b minha-nova-funcionalidade
   ```

3. Faça suas alterações e commit:

   ```bash
   git commit -am 'Adiciona nova funcionalidade'
   ```

4. Envie para o repositório remoto:

   ```bash
   git push origin minha-nova-funcionalidade
   ```

5. Abra um **Pull Request**.

## Licença

Distribuído sob a licença MIT. Veja o arquivo **LICENSE** para mais informações.

Feito com ❤️ por Mell Karine.
