from database import abrir_conexion
from flask import Flask
from flask import jsonify
from flask import request

conexion= abrir_conexion()

app = Flask(__name__)

@app.route('/metodos', methods=['GET', 'POST', 'DELETE', 'PUT'])
def variable_metodos():
    if request.method == 'POST':
        return create_person()
    elif request.method == 'GET':
        return get_person()


def create_person():
    try:
        content = request.get_json(force=True)
        cur = conexion.cursor()
        query = "INSERT INTO person (name, last_name, phone) VALUES (%s, %s, %s)"
        cur.execute(query, (content['name'], content['last_name'],content['phone']))
        conexion.commit()
        cur.close()

        return jsonify({'mensaje': 'Datos insertados correctamente'})
    except Exception as e:
        
        return jsonify({'error': str(e)})

def get_person():
    try:
         # Crear un cursor para ejecutar consultas
            cur = conexion.cursor()
            query = "SELECT * FROM person"
            cur.execute(query)
            formulario = cur.fetchall()

            data = [{'id': row[0], 'name': row[1], 'last_name': row[2], 'phone': row[3]} for row in formulario]

            # Cerrar el cursor y la conexión
            cur.close()
            # conexion.close()

            # Devolver la información en formato JSON
            return jsonify({'personas': data})
    except Exception as e:
        
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)