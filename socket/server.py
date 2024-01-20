import socket

socketServer = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0,fileno=None)

hosName = '127.0.0.1' 
numberPort = 8080

socketServer.bind((hosName,numberPort))

print("Socket obtenido la dirección {} y el puerto {}".format(hosName,numberPort))
socketServer.listen(2)

while True:
    client ,client_ddr = socketServer.accept()
    print('La conexion se establecion en el cliente: {}'.format(client_ddr))

    msg = client.recv(1024).decode('utf8')
    print('Mensaje recibido del cliente {}'.format(msg))

    print('Enviando respuesta al cliente ')
    msg_out = 'mensaje enviado {}'.format(msg).encode('utf8')
    client.send(msg_out)
    client.close()
    break