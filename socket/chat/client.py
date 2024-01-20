import socket
import threading

def handle_messages():
    while True:
        msg = s.recv(1024)
        print('mensaje recibido', msg.decode())


def send_message():
    while True:
        mnsg = input('ingresar mensaje')
        s.sendall(mnsg.encode())

if __name__ == '__main__':
    s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    s.connect(('192.168.20.214',9090))

    thread_recive = threading.Thread(target=handle_messages)
    thread_send = threading.Thread(target=send_message)

    thread_recive.start()
    thread_send.start()