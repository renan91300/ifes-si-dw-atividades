# Faça um programa que declare uma lista com ao menos 10 números inteiros, com pelo menos 3 deles repetidos. Em seguida, converta essa lista para um conjunto, visando eliminar os itens repetidos, converta de volta para uma lista, e mostre o resultado na tela.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

print('Lista original:', lista)

conjunto = set(lista)
print('Conjunto:', conjunto)

lista = list(conjunto)

print('Lista sem repetições:', lista)