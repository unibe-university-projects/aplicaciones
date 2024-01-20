import socket

socketClient = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM,proto=0,fileno=None)

hosName = '127.0.0.1' 
numberPort = 8080

socketClient.connect((hosName,numberPort))

print('Conexión cliente esblecida')

msg = 'hola servidor'.encode('utf8')
socketClient.send(msg)

msg_out = socketClient.recv(1024).decode('utf8')
print('El mensaje fue enviado al servidor')
print(msg_out)
print('Cierra la conexión')