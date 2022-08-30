 Projeto 1
 Implementação de cliente e servidor UDP comum utilizando a biblioteca Socket na linguagem Python, com envio de arquivo (daremos uma pasta de arquivos que devem funcionar) e devolução.

Instruções de execução:
SERVIDOR:
1- Quando ativar o Servidor vai ser criado um socket UDP:
    -maquinaSocket = socket(AF_INET, SOCK_DGRAM) -> Cria o socket
    -AF_INET -> Indica o tipo de IP a ser utilzado, nesse caso, IPV4
    -SOCK_DGRAM -> Indica o protocolo UDP
2- Liga o socket a porta local:
    -maquinaSocket.bind((ip, porta)) -> Liga o socket, forçando no ip e porta selecioandos (em uma tupla)
3- Servidor vai ficar "escutando"

CLIENTE:
4-Quando ativar o Cliente vai ser criado um socket UDP para o servidor:
    -maquinaSocket = socket(AF_INET, SOCK_DGRAM) -> Cria o socket
    -AF_INET -> Indica o tipo de IP a ser utilzado, nesse caso, IPV4
    -SOCK_DGRAM -> Indica o protocolo UDP
5- Pede nome do arquivo ao usuario 
6- Usuario digita o nome do arquivo desejado.
7-Do lado do servidor existem 3 arquivos que podem ser solicitados: dog.pdf, creeper.jpg e texte.txt
8- Caso o cliente digite "nenhum", a execução do lado do cliente é finalizada.
9-No codigo, é transformado os strings em bytes por meio do metodo encode().
10- Envia o datagrama com Ip e numero da porta do servidor pela função sendto() em uma tupla:
    clienteSocket.sendto(msg_enc, endereco_servidor).

SERVIDOR:
11-Lê datagrama do socket UDP,obtendo endereço do cliente:
    -maquinaSocket.recvfrom(TAM_BUFFER) -> Tem como retorno: dados em bytes, e uma tupla contendo (ip, porta) de quem enviou as informações
12- Transforma os bytes em string,com o metodo decode():
    msg_dec = msg.decode()
13-Tenta abrir arquivo, e retorna em bytes para o cliente.Observação, tem um tratamento de erro(try-catch), caso tenha erro, servidor envia string vazio para Cliente.
14-Por ultimo servidor envia string vazio para cliente com intuito de desbloquear a funcao recvfrom no Cliente.

CLIENTE
15-Lê datagrama recebido do Servidor:
    leitura_buffer, endereco_servidor = clienteSocket.recvfrom(1000000)
    E recebe o buffer e o endereco do servidor.
16-Usa o condicional if para verificar se ouve algum erro na abertura do arquivo no servidor.
17-Se nao, escreve o arquivo recebido que foi tranformado em bytes.
18- Fecha o socket no lado do Cliente.


