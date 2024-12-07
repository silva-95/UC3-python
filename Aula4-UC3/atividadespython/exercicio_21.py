# Crie uma classe Livro com atributos titulo e autor. Sobrescreva o método especial __str__ para que, ao usar print em um objeto da classe, ele exiba o título e o autor do livro no formato: "Título: <titulo>, Autor: <autor>"

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        print(f'Título: {self.titulo}, Autor: {self.autor}')
    
livro1 = Livro('O Senhor dos Aneis', 'JRR Tolkien')
print(livro1)    
