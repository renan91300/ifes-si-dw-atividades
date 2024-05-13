import datetime

agora = datetime.datetime.now()

formatado = agora.strftime("%A, %d de %B de %Y %H:%M")

print(formatado)