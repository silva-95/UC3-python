# Crie uma classe Funcionario com os atributos nome, horas_trabalhadas e valor_hora.
# Adicione os métodos:
# registrar_horas(horas) para registrar horas trabalhadas.
# calcular_pagamento() para calcular o pagamento baseado nas horas trabalhadas e no valor por hora.

class Funcionario:
    def __init__(self, nome, valor_hora):
        self.nome = nome
        self.horas_trabalhadas = 0  
        self.valor_hora = valor_hora  
    
    def registrar_horas(self, horas):
        """Registra as horas trabalhadas."""
        self.horas_trabalhadas += horas
    
    def calcular_pagamento(self):
        """Calcula o pagamento baseado nas horas trabalhadas e no valor por hora."""
        return self.horas_trabalhadas * self.valor_hora
    
    def exibir_detalhes(self):
        """Exibe o nome, horas trabalhadas e o pagamento calculado."""
        pagamento = self.calcular_pagamento()
        print(f"Nome: {self.nome}")
        print(f"Horas trabalhadas: {self.horas_trabalhadas}")
        print(f"Pagamento: R${pagamento:.2f}")

# Exemplo de uso:
valor_hora = 28.30  

funcionario1 = Funcionario(input(f"DIGITE O NOME DO FUNCIONÁRIO: "), valor_hora)
funcionario1.registrar_horas(int(input(f"QUANTAS HORAS O FUNCIONÁRIO TRABALHOU: ")))
funcionario1.exibir_detalhes()

funcionario2 = Funcionario(input(f"DIGITE O NOME DO FUNCIONÁRIO: "), valor_hora)
funcionario2.registrar_horas(int(input(f"QUANTAS HORAS O FUNCIONÁRIO TRABALHOU: ")))
funcionario2.exibir_detalhes()
