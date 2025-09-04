# Importa o módulo os para manipulação de arquivos e diretórios
import os
import shutil

# Cria uma variável com o caminho da pasta que você quer organizar
pasta = "./fakefiles"

# Organiza os arquivos em subpastas com base na extensão
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".doc") or arquivo.endswith(".docx"):
            shutil.move(f"{pasta}/{arquivo}", f"{pasta}/doc/{arquivo}")
    elif arquivo.endswith(".pdf"):
            shutil.move(f"{pasta}/{arquivo}", f"{pasta}/pdf/{arquivo}")
    elif arquivo.endswith(".html"):
            shutil.move(f"{pasta}/{arquivo}", f"{pasta}/html/{arquivo}")
    elif arquivo.endswith(".txt"):
            shutil.move(f"{pasta}/{arquivo}", f"{pasta}/txt/{arquivo}")
''
