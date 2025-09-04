'''
Programa para organizar arquivos em pastas com base em suas extensões.
'''

import os
import shutil

# Dicionário mapeando extensões de arquivos para pastas
extensoes_para_pastas = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv'],
    'Musicas': ['.mp3', '.wav', '.aac', '.flac'],
    'Arquivos Comprimidos': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.java', '.c', '.cpp'],
}  

# Função para organizar arquivos
def organizar_arquivos(diretorio):
    if not os.path.isdir(diretorio):
        print(f"O diretório {diretorio} não existe.")
        return

    for item in os.listdir(diretorio):
        item_path = os.path.join(diretorio, item)
        
        if os.path.isfile(item_path):
            extensao = os.path.splitext(item)[1].lower()
            pasta_destino = None
            
            for pasta, extensoes in extensoes_para_pastas.items():
                if extensao in extensoes:
                    pasta_destino = pasta
                    break
            
            if pasta_destino:
                pasta_destino_path = os.path.join(diretorio, pasta_destino)
                
                if not os.path.exists(pasta_destino_path):
                    os.makedirs(pasta_destino_path)
                
                shutil.move(item_path, os.path.join(pasta_destino_path, item))
                print(f'Movido: {item} -> {pasta_destino}/')
            else:
                print(f'Extensão desconhecida para o arquivo: {item}')
        else:
            print(f'Ignorando diretório: {item}')