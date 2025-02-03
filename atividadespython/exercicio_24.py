# Implemente uma classe Temperatura com os atributos celsius.
# Adicione métodos para:
# Converter para Fahrenheit (converter_para_fahrenheit).
# Converter para Kelvin (converter_para_kelvin).

class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        
    def converter_para_fahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        print(f"{self.celsius} graus Celsius equivalem a {fahrenheit} graus Fahrenheit.")
        
    def converter_para_kelvin(self):
        kelvin = self.celsius + 273.15
        print(f"{self.celsius} graus Celsius equivalem a {kelvin} graus Kelvin.")

Temperatura1 = Temperatura(25)
Temperatura1.converter_para_fahrenheit()
Temperatura1.converter_para_kelvin()

Temperatura2 = Temperatura(30)
Temperatura2.converter_para_fahrenheit()
Temperatura2.converter_para_kelvin()   

