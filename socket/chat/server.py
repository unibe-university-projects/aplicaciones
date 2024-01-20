import socket
import threading


def handle_messages(client_socket):
    while True:
        msg = client_socket.recv(1024).decode('utf')
        if not msg:
            break
        broadcast(msg)

def broadcast(msg):
    for client in clients:
        client.send(msg)

def server_chat():
    s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    s.bind(('192.168.20.215',8080))
    s.listen(9)
    print ('servidor espera la conexión')

    while True:
        client_socket , client_drr = s.accept()
        print('Conexion establecida {}'.format(client_drr))
        clients.append(client_socket)

        thr = threading.Thread(target=handle_messages,args=(client_socket,))
        thr.start()
        
if __name__ == '__main__':
    clients = []
    server_chat()