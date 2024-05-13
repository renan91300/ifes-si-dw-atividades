nome_produto = input("Digite o nome do produto: ")
preco_custo = float(input("Digite o preço de custo do produto: "))
preco_venda = float(input("Digite o preço de venda do produto: "))
quantidade_estoque = int(input("Digite a quantidade em estoque do produto: "))

lucro = (preco_venda - preco_custo) * quantidade_estoque

print(f"O lucro ao vender todo o estoque de {nome_produto} será de: {lucro}")