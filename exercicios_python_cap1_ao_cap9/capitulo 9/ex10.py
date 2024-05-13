def importar_modulo(nome_modulo: str) -> None:
    try:
        __import__(nome_modulo)
        print("Módulo importado com sucesso!")
    except ModuleNotFoundError:
        print("Módulo não encontrado!")
    finally:
        print("Operação finalizada!")

importar_modulo("math")
importar_modulo("teste")