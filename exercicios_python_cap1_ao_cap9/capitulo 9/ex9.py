def read_file(filename: str) -> None:
    try:
        file = open(filename, "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    finally:
        print("Fim da execução!")
    

read_file("arquivo.txt")