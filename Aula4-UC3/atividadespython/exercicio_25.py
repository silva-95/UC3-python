# Crie uma classe Tarefa com os atributos descricao e status (inicialmente "pendente").
# Adicione métodos para:
# Alterar o status para "concluída" (marcar_como_concluida).
# Exibir os detalhes da tarefa (exibir_tarefa).

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.status = "pendente"
    
    def marcar_como_concluida(self):
        self.status = "concluída"
    
    def exibir_tarefa(self):
        print(f"Descrição: {self.descricao}")
        print(f"Status: {self.status}")

# Exemplo de uso:
tarefa1 = Tarefa("Estudar para a prova")
tarefa1.exibir_tarefa()

tarefa2 = Tarefa("Ler um livro")
tarefa2.marcar_como_concluida()

tarefa3 = Tarefa("Fazer exercícios de programação")
tarefa3.exibir_tarefa()

tarefa4 = Tarefa("Passear com o cachorro")
tarefa4.marcar_como_concluida()


# Alterando o status da tarefa para "concluída"
tarefa1.marcar_como_concluida()
tarefa1.exibir_tarefa()


            