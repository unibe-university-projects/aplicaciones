import psycopg2
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def verificar_existencia_base_datos(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (os.getenv('DB_DATABASE'),))
            
            if cursor.fetchone():
                print(f"Conexión exitosa a la base de datos: {os.getenv('DB_DATABASE')}")
            else:
                print(f"La base de datos '{os.getenv('DB_DATABASE')}' no existe.")
    except Exception as e:
        print(f"Error al verificar la existencia de la base de datos: {e}")

def abrir_conexion():
    try:
        conexion = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )

        verificar_existencia_base_datos(conexion)
        return conexion
    except Exception as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return None  # Devuelve None en caso de error

def cerrar_conexion(conexion):
    if conexion is not None:
        conexion.close()


if __name__ == "__main__":
    conexion = abrir_conexion()
    
    # Realizar operaciones con la conexión
    
    cerrar_conexion(conexion)
