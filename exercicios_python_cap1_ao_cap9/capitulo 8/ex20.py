class Fracao():
    def __init__(self, numerador, denominador) -> None:
        self.numerador = numerador
        self.denominador = denominador

    def mostrar_dados(self):
        print(f"{self.numerador}/{self.denominador}")

    def multiplicar(self, fracao: "Fracao"):
        return Fracao(self.numerador * fracao.numerador, self.denominador * fracao.denominador)


fracao = Fracao(2, 3)
fracao2 = Fracao(3, 4)

fracao.multiplicar(fracao2).mostrar_dados()