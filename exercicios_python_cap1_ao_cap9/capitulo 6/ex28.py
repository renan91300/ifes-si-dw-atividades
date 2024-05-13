def pega_palavras(frase):
    yield from frase.split()

texto = input('Digite um texto: ')

print('Palavras:', list(pega_palavras(texto)))