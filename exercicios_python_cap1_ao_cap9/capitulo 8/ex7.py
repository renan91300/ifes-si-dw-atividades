class Pessoa():
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario) -> None:
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nSalário: {self.salario}")
    

pessoas = [
    Pessoa("João", 20),
    Pessoa("Maria", 30),
    Funcionario("José", 40, 1000),
    Funcionario("Ana", 50, 2000)
]

for pessoa in pessoas:
    if type(pessoa) == Funcionario:
        pessoa.mostrar_dados()