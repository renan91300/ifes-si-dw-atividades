# Faça um programa que crie um diretório chamado "Textos" e que, dentro desse diretório, crie 3 arquivos com os nomes "arquivo1.txt", "arquivo2.txt" e "arquivo3.txt" todos contendo o texto "Python Essencial". Em seguida, o programa deve criar um arquivo compactado (.zip) contendo o diretório "Textos".

import os
import zipfile

os.mkdir("Textos")

with open("Textos/arquivo1.txt", "w", encoding="utf-8") as arquivo1:
    arquivo1.write("Python Essencial")

with open("Textos/arquivo2.txt", "w", encoding="utf-8") as arquivo2:
    arquivo2.write("Python Essencial")

with open("Textos/arquivo3.txt", "w", encoding="utf-8") as arquivo3:
    arquivo3.write("Python Essencial")

with zipfile.ZipFile("Textos/arquivo.zip", "w", 
  compresslevel=9, compression=zipfile.ZIP_DEFLATED) as arquivo_zip: 
  arquivo_zip.write("Textos/arquivo1.txt") 
  arquivo_zip.write("Textos/arquivo2.txt") 
  arquivo_zip.write("Textos/arquivo3.txt") 
 