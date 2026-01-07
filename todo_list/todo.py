
def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + "\n")

tarefas = []

def mostrar_menu():
    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa}")
    elif opcao == "3":
        if not tarefas:
            print("Não há tarefas para remover.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa}")
            numero = int(input("Digite o número da tarefa para remover: "))
            if 1 <= numero <= len(tarefas):
                tarefa_removida = tarefas.pop(numero - 1)
                print(f"Tarefa '{tarefa_removida}' removida!")
            else:
                print("Número inválido.")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            for linha in arquivo:
                tarefas.append(linha.strip())
    except FileNotFoundError:
        pass