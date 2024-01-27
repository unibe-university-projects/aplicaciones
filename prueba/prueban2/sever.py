import socket

def suma_sucesiva(n):
    return sum(range(1, n+1))

def main():

    host = '192.168.20.215'
    port = 8080

    # Crear un socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    server_socket.bind((host, port))
    print(f"Servidor escuchando en {host}:{port}")

    while True:

        data, client_address = server_socket.recvfrom(1024)

        num = int(data.decode('utf-8'))

        resultado = suma_sucesiva(num)

        server_socket.sendto(str(resultado).encode('utf-8'), client_address)

if __name__ == "__main__":
    main()
