class Veiculo():
    def __init__(self) -> None:
        pass

    def acelerar(self):
        print("Acelerando...")
    
    def frear(self):
        print("Freando...")
    
    def exibir_velocidade(self):
        print("Velocidade: 30 km/h")
    

class Carro(Veiculo):
    def __init__(self, marca) -> None:
        self.marca = marca

carro = Carro("Fiat")
carro.acelerar()
carro.frear()
carro.exibir_velocidade()