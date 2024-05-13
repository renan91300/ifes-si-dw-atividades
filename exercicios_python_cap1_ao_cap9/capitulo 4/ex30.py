import datetime

agora = datetime.datetime.now()

semana = agora.strftime("%U")

print(f"A semana atual do ano é: {semana}")