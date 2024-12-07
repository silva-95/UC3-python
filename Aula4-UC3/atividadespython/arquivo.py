# Criando ou abrindo um arquivo para escrita
with open("dados.txt", "w") as arquivo:
    arquivo.write("Curso: Programação em Python\n")
    arquivo.write("Aluno: Maria\n")
    arquivo.write("Progresso: 85%\n")

# Lendo o conteúdo do arquivo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do Arquivo:")
    print(conteudo)

# Adicionando informações ao arquivo
with open("dados.txt", "a") as arquivo:
    arquivo.write("Projeto: Sustentabilidade Digital\n")
