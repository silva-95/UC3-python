# Crie uma classe Filme com os atributos titulo, genero e duracao (em minutos).
# Implemente um método especial para exibir os detalhes do filme de forma legível.

class Filme:
    def __init__(self, titulo, genero, duracao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao  

    def exibir_detalhes(self):
        print(f'Titulo: {self.titulo}, Genero: {self.genero}, Duracao: {self.duracao}')

# exemplo de uso
filmes = [
    Filme('Filme 1', 'Ação', 120),
    Filme('Filme 2', 'Romance', 90),
    Filme('Filme 3', 'Drama', 150)
]

for filme in filmes:    
    filme.exibir_detalhes()

filme1 = Filme('Filme 1', 'Ação', 120)
filme1.exibir_detalhes()

filme2 = Filme('Filme 2', 'Romance', 90)
filme2.exibir_detalhes()

filme3 = Filme('Filme 3', 'Drama', 150)
filme3.exibir_detalhes()


   