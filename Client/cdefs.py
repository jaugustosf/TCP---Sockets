from datetime import datetime
from psutil import *
from GPUtil import *
import os

FORMAT = 'utf-8'
SIZE = 2048
PATH = "./Server/Archives"
#Client functions
def menu():
    print(
""" 
OPÇOES:
1 - DADOS DO SERVER: 
2 - HORA ATUAL:
3 - BAIXAR ARQUIVO:
4 - LISTAR ARQUIVOS:
5 - SAIR:
""")
    
# def get_files():
#     try:        
#         print(fileName)
#         parts = fileName.split(' ', 1)
#         fileName = parts[0]
#         fileContent = parts[1]

#         pathFile = os.path.join(os.getcwd(), fileName)
#         with open(pathFile, 'wb') as file:
#             file.write(fileContent.encode('utf-8'))

#         print(f'Arquivo {fileName} recebido e salvo localmente!')

#     except Exception as e:
#         error_message = f'Erro ao enviar/receber dados: {str(e)}'
#         print(error_message)
#         return error_message

# def verify():
#     fileName = request.split(' ')[1]

#     # Verifica se o arquivo existe no diretório
#     pathFile = os.path.join(PATH, fileName)
#     if os.path.exists(pathFile) and os.path.isfile(pathFile):
#         with open(pathFile, 'rb') as file:
#             fileContent = file.read()
#         return f'{fileName} {fileContent.decode(FORMAT)}'

#     return f'{fileName} não encontrado no diretório.'