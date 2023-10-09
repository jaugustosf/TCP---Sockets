from socket import *
import os

from c_Functions import menu

HOST = '127.0.0.1'
PORT = 8080
FORMAT = 'utf-8'
SIZE = 100000

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

def send_request(command):
    client.send(command.encode(FORMAT))
    response = client.recv(SIZE).decode(FORMAT)

    if response.startswith('3'):
        parts = response.split(' ', 2)
        fileName = parts[1]
        fileContent = parts[2]

        filePath = os.path.join(os.getcwd(), fileName)
        with open(filePath, 'wb') as file:
            file.write(fileContent.encode("latin-1"))

        print(f'Arquivo {fileName} recebido e salvo localmente!')
    else:
        print(f"\nResposta: {response}")

while True:
    try:
        menu()
        option = str(input("Escolha um comando (1-5): "))

        if option == "1":
            response = send_request("1")
        elif option == "2":
            response = send_request("2")
        elif option.startswith("3"):
            fileName = option.split(' ')[1]
            response = send_request('3 ' + fileName)
        elif option == "4":
            response = send_request("4")
        elif option == "5":
            print("Fechando conexão com servidor")
            client.close()
            break
        else:
            response = 'Comando inválido.'

    except KeyboardInterrupt:
        client.close()