from flask import Flask, jsonify
from util import obter_cidades_por_estado, obter_todas_cidades

app = Flask(__name__)

@app.route('/listar-cidades/brasil', methods=['GET'])
def listar_cidades_brasil():
    todas_as_cidades = obter_todas_cidades()
    return jsonify(
        todas_as_cidades
    )

@app.route('/listar-cidades/estado', methods=['GET'])
def listar_cidades_por_estado():
    resposta = obter_cidades_por_estado()
    return jsonify(
        resposta
    )

if __name__ == '__main__':
    app.run(debug=False)
