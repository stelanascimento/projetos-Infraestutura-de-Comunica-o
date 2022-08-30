from socket import *
from time import *

#Endereco do servidor
PORTA_SERVIDOR = 7777
IP_SERVIDOR = "localhost"
endereco_servidor = (IP_SERVIDOR, PORTA_SERVIDOR)

#Ligar o socket com o ip e porta selecionados
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(endereco_servidor)

print("Socket do servidor ligado.")

while True:
    #Esperar algum cliente enviar informacao
    print("Esperando clientes...")
    msg, endereco_cliente = serverSocket.recvfrom(1000000)
    msg_dec = msg.decode()
    print("Mensagem recebida.")

    #Tentar abrir arquivo pedido
    try:
        with open(msg_dec, "rb") as arquivo:
            print("Arquivo encontrado.")
            print("Enviando arquivo...")
            #Laco de leitura e envio do arquivo
            for dados in arquivo.readlines():
                serverSocket.sendto(dados, endereco_cliente)
                #Sleep necessário para sincronizar e enviar corretamente o arquivo
                sleep(0.00000001)
        print("Arquivo enviado.\n")
    #Caso o arquivo na exista, informar
    except:
        serverSocket.sendto("".encode(), endereco_cliente)
        print("Arquivo não encontrado.\n")

    #Envio de informação vazia para desbloquear a funcao recvfrom() no cliente
    serverSocket.sendto("".encode(), endereco_cliente)
