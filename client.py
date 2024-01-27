import socket
from PIL import Image
import os

host = '192.168.56.1'
puerto = 8081
margin = 200

image_path = 'imagen_a_enviar.jpg'
image_size = os.path.getsize(image_path)
BUFFER_SIZE = image_size + margin
print('tamaño de la imagen en bytes', BUFFER_SIZE)

# Crear un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, BUFFER_SIZE)

# Cargar la imagen
image_path = 'imagen_a_enviar.jpg'
image = Image.open(image_path)

# Obtener el tamaño de la imagen
image_size = len(image.tobytes())  # método tobytes obtiene una representación de bytes de la imagen
print('imagen', image_size)

# Enviar el tamaño de la imagen al servidor
client_socket.sendto(str(BUFFER_SIZE).encode(), (host, puerto))

# Enviar la imagen al servidor 
with open(image_path, 'rb') as file:
    image_data = file.read()
    client_socket.sendto(image_data, (host, puerto))
    print(f"Imagen enviada correctamente")

# Cerrar socket
client_socket.close()
