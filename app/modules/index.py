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
        return jsonify('soy get')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)