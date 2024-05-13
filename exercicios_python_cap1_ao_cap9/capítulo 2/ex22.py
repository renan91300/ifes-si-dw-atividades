clima = input("Como está o clima (ensolarado, chuvoso, nublado)? ")

match clima:
    case "ensolarado":
        print("Use óculos de sol.")
    case "chuvoso":
        print("Leve guarda-chuva.")
    case "nublado":
        print("Vista um casaco.")
    case _:
        print("Não entendi.")