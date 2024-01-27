from  flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/ejemplo', methods=['GET'])
def json():
    array = ['pera','manzana','mangos']
    return jsonify(Hola = array)


if __name__ == '__main__':
    app.run(debug=True,host='192.168.56.1',port='8080')