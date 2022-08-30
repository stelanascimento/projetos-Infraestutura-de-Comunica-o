from socket import *
continuar = True
# Servidor de destino
PORTA_SERVIDOR = 7777
IP_SERVIDOR = 'localhost'
endereco_servidor = (IP_SERVIDOR, PORTA_SERVIDOR)

while continuar:
    # Criacao do socket
    clienteSocket = socket(AF_INET, SOCK_DGRAM)

    # Input de informacao do cliente
    msg = str(input("Pedido: "))
    if msg == 'nenhum':
        print("Parando...")
        clienteSocket.close()
        continuar = False
        break

    msg_enc = msg.encode()

    # Envio do pedido para o servidor
    clienteSocket.sendto(msg_enc, endereco_servidor)

    # Primeira leitura do que recebeu
    leitura_buffer, endereco_servidor = clienteSocket.recvfrom(1000000)

    # Se o envio for vazio, avisar que o arquivo nao foi encontrado
    if(not leitura_buffer):
        print("Arquivo não encontrado.")
    # Se nao, escrever o arquivo recebido
    else:
        with open(msg, "wb") as arquivo:
            # Enquanto a leitura não for nula, escrever
            while (leitura_buffer):
                arquivo.write(leitura_buffer)
                leitura_buffer, endereco_servidor = clienteSocket.recvfrom(
                    1000000)

        print("Arquivo Recebido!\n")

    # Destruir socket
    clienteSocket.close()

# clienteSocket.setblocking(0) -> Desbloqueia
# clienteSocket.setblocking(0) -> Bloqueia
