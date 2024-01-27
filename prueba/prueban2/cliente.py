import socket

def sucesion():

    host = '192.168.20.215'
    port = 8080

    # Crear un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:

        num = input("Ingrese un número para la suma: ")
        if num == '0':
            break


        print('entra ', num)
        client_socket.sendto(str(num).encode(), (host, port)) 

        
        data, _ = client_socket.recvfrom(1024)
        resultado = int(data.decode('utf-8'))

        print(f"Resultado de la suma sucesiva: {resultado}")


    client_socket.close()

if __name__ == "__main__":
    sucesion()
