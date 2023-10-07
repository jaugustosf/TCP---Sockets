from socket import *
import os

from cdefs import menu

HOST = '127.0.0.1'
PORT = 8080
FORMAT = 'utf-8'
SIZE = 2048

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

# Função para enviar comandos ao servidor e receber respostas
def send_request(command):
    try:
        client.send(command.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')

        if response:
            if 'ARQUIVO' in response and 'não encontrado no diretório.' in response:
                print(response)
            elif response.startswith('ARQUIVO'):
                parts = response.split(' ', 2)
                arquivo_nome = parts[1]
                arquivo_conteudo = parts[2]

                caminho_arquivo = os.path.join(os.getcwd(), arquivo_nome)
                with open(caminho_arquivo, 'wb') as arquivo:
                    arquivo.write(arquivo_conteudo.encode('utf-8'))

                print(f'Arquivo {arquivo_nome} recebido e salvo localmente!')
            else:
                print(response)
        else:
            print('Resposta vazia recebida do servidor.')


    except Exception as e:
        error_message = f'Erro ao enviar/receber dados: {str(e)}'
        print(error_message)
        return error_message

while True:
    try:
        menu()
        option = str(input("Escolha um comando (1-5): "))

        if option == "1":
            response = send_request("1")
        elif option == "2":
            response = send_request("2")
        elif option.startswith("3"):
            nome_arquivo = option.split(' ')[1]
            response = send_request('ARQUIVO ' + nome_arquivo)
        elif option == "4":
            response = send_request("4")
        elif option == "5":
            print("Fechando conexão com servidor")
            client.close()
            break
        else:
            response = 'Comando inválido.'

        print(f"\nResposta: {response}")

    except KeyboardInterrupt:
        client.close()