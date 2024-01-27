import socket
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import os

host = '192.168.56.1'
puerto = 8081
margin = 200

image_path = 'imagen_a_enviar.jpg'
image_size = os.path.getsize(image_path)
BUFFER_SIZE = image_size + margin

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFFER_SIZE)

server_socket.bind((host, puerto))

print(f"Servidor esperando conexiones en {host}:{puerto}")

try:
    # Recibir el tamaño de la imagen
    print('entra aqui')
    image_size_data, client_address = server_socket.recvfrom(1024)
    received_image_size = int(image_size_data.decode())
    print('entra size', received_image_size)

    # Recibir la imagen
    received_image = b''
    print(received_image)
    while len(received_image) < received_image_size:
        data, _ = server_socket.recvfrom(BUFFER_SIZE)
        received_image += data
        print('entra al bucle', len(received_image))

        print(f"Tamaño de la imagen recibido: {received_image_size} bytes")

        # Mostrar la imagen
        image = Image.open(BytesIO(received_image))
        # print('muestraaaaa',image)
        # Utilizar matplotlib para mostrar la imagen
        plt.imshow(image)
        plt.show()

        print("Imagen mostrada correctamente")

except socket.error as e:
    print(f"Error de socket: {e}")

except Exception as e:
    print(f"Error en el servidor: {e}")

finally:
    # Cerrar el socket del servidor
    server_socket.close()
