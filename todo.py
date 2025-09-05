# Lista para armazenar as tarefas
tarefas = []

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\n--- Tarefas ---")
        for i, t in enumerate(tarefas):
            status = "✅" if t["concluida"] else "❌"
            print(f"{i+1}. {t['descricao']} [{status}]")

def adicionar_tarefa():
    desc = input("Descrição da tarefa: ")
    tarefas.append({"descricao": desc, "concluida": False})
    print("Tarefa adicionada!")

def concluir_tarefa():
    listar_tarefas()
    try:
        i = int(input("Número da tarefa concluída: ")) - 1
        if 0 <= i < len(tarefas):
            tarefas[i]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def remover_tarefa():
    listar_tarefas()
    try:
        i = int(input("Número da tarefa a remover: ")) - 1
        if 0 <= i < len(tarefas):
            del tarefas[i]
            print("Tarefa removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Digite um número válido.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas()
        elif opcao == "2":
            adicionar_tarefa()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Executar o menu
menu()
