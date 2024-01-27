import socket
from PIL import Image #biblioteca PIL para manipular imagenes

# Configuración del cliente
host = '127.0.0.1'
puerto = 8081

# Crear un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Cargar la imagen
image_path = 'imagen_a_enviar.jpg'
image = Image.open(image_path)

# Obtener el tamaño de la imagen
image_size = len(image.tobytes()) #metodo tobytes obtiene una representacion de bytes de la imagen

# Enviar el tamaño de la imagen al servidor
client_socket.sendto(str(image_size).encode(), (host, puerto))

# Enviar la imagen al servidor 
with open(image_path, 'rb') as file:
    image_data = file.read(1024)
    while image_data:
        client_socket.sendto(image_data, (host, puerto))
        image_data = file.read(1024)

print(f"Imagen enviada correctamente")

# Cerrar socket
client_socket.close()





































































