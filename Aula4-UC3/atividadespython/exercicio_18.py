# Implemente funções que gerenciam um sistema de lista de alunos:
# Adicionar um aluno.
# Remover um aluno.
# Exibir todos os alunos.


def adicionar_aluno(alunos, aluno):
    alunos.append(aluno)
    print("Aluno adicionado com sucesso!")
    return alunos


def remover_aluno(alunos, aluno):
    alunos.remove(aluno)
    print("Aluno removido com sucesso!")
    return alunos


def exibir_alunos(alunos):
    for aluno in alunos:
        print(aluno)
    return alunos


alunos = []

while True:
    print("Escolha uma opção:")
    print("1 - Adicionar aluno")
    print("2 - Remover aluno")
    print("3 - Exibir alunos")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        aluno = input("Digite o nome do aluno: ")    
        alunos = adicionar_aluno(alunos, aluno) 

    elif opcao == "2":
        aluno = input("Digite o nome do aluno que deseja remover: ")
        alunos = remover_aluno(alunos, aluno)

    elif opcao == "3":
        alunos = exibir_alunos(alunos)

    elif opcao == "4": 
        break