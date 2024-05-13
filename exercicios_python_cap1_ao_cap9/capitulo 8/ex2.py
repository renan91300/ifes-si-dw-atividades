class Retangulo():
    def __init__(self, altura, largura) -> None:
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura
    

retangulo = Retangulo(10, 20)
print(f"A área do retângulo é: {retangulo.area()}")