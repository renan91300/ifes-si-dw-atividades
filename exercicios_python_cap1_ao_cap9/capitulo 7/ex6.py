import shutil

def copia_arquivo():
    
    nome_arquivo = input("Digite o nome do arquivo que deseja copiar: ")
    novo_nome_arquivo = nome_arquivo.split('.')[0] + ".cópia"

    try:
        shutil.copy(nome_arquivo, novo_nome_arquivo)
        print("Arquivo copiado com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

copia_arquivo()