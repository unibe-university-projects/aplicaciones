from database import abrir_conexion
from flask import Flask
from flask import jsonify
from flask import request

conexion= abrir_conexion()

app = Flask(__name__)

@app.route('/metodos', methods=['GET', 'POST', 'DELETE', 'PUT'])
def variable_metodos():
    if request.method == 'POST':
        content = request.get_json(force=True)
        print(content)
        if 'nombre' in content.keys():
            nombre = content['nombre']
        else:
            return jsonify(error='Json no es correcto')
        if 'apellido' in content.keys():
            apellido = content['apellido']
        else:
            return jsonify('json no es correcto')
        return jsonify('quien eres ? : ' + nombre + apellido)
    elif request.method == 'GET':
        try:
            # Crear un cursor para ejecutar consultas
            cur = conexion.cursor()
            query = "SELECT * FROM person"
            cur.execute(query)
            formulario = cur.fetchall()

            data = [{'id': row[0], 'nombre': row[1], 'apellido': row[2]} for row in formulario]

            # Cerrar el cursor y la conexión
            cur.close()
            conexion.close()

            # Devolver la información en formato JSON
            return jsonify({'personas': data})

        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir
            return jsonify({'error': str(e)})


# def get_person()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)