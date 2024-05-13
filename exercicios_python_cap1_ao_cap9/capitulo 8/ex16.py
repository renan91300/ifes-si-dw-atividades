class Produto():
    def __init__(self, nome, preco, estoque) -> None:
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nPreço: {self.preco}\nEstoque: {self.estoque}")


class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, imposto) -> None:
        super().__init__(nome, preco, estoque)
        self.imposto = imposto
    

    def preco_final(self):
        return self.preco + (self.preco * (self.imposto / 100))
    

produto = ProdutoImportado("Notebook", 3000, 10, 10)

produto.mostrar_dados()
print(f"Preço final: {produto.preco_final()}")