qtd_tarefas = int(input("Digite quantas tarefas deseja cadastrar: "))

lista_tarefas = []

for i in range(qtd_tarefas):
    nome_tarefa = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(nome_tarefa)

banco_dados_tarefas = []

for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):

    prazo_dias = id_tarefa * 2

    status = "Pendente"

    banco_dados_tarefas.append(
        (id_tarefa, nome_tarefa, prazo_dias, status)
    )

print("\n--- RESUMO DO SISTEMA ---")

for id_tarefa, nome_tarefa, prazo_dias, status in banco_dados_tarefas:
    print(
        f"ID: {id_tarefa} | "          
        f"Tarefa: {nome_tarefa} | "
        f"Prazo: {prazo_dias} dias | "
        f"Status: {status}"
    )

print(f"\nTotal de tarefas cadastradas: {len(banco_dados_tarefas)}")
