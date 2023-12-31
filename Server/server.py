from socket import *
import threading
import os

from s_Functions import get_hour, get_info, list_files

PATH = "./Server/archives"

HOST = 'localhost'
PORT = 8080
FORMAT = 'utf-8'
SIZE = 100000

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print('Servidor pronto para receber conexões...')

# Função para lidar com as conexões dos clientes
def handleClient(clientSocket):
    while True:
        request = clientSocket.recv(SIZE).decode(FORMAT)
        if not request:
            break

        response = process_request(request)
        
        clientSocket.send(response.encode(FORMAT))
            
    clientSocket.close()

# Função para processar a requisição do cliente
def process_request(request):
    if request == "1":
        print("Enviando informações...")
        return get_info()

    elif request == "2":
        print("Enviando hora atual...")
        return get_hour()
    
    elif request.startswith("3"):
        fileName = request.split(' ')[1]

        # Verifica se o arquivo existe no diretório
        filePath = os.path.join(PATH, fileName)
        if os.path.exists(filePath) and os.path.isfile(filePath):
            with open(filePath, 'rb') as file:
                fileContent = file.read()
            return f'3 {fileName} {fileContent.decode("latin-1")}'

        return f'3 {fileName} não encontrado no diretório.'
    
    
    elif request == "4":
        print("Listando arquivos...")
        files = list_files(PATH)

        return files
    
    elif request == "5":
        return 'Conexão encerrada.'
    
    else:
        return 'Comando não reconhecido.'

# Loop para aceitar múltiplas conexões
while True:
    client_socket, addr = server.accept()
    print(f'Conexão estabelecida com {addr}')
    client_handler = threading.Thread(target=handleClient, args=(client_socket,))
    client_handler.start()