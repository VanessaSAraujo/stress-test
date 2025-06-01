from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/cep/<cep>')
def consultar_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'Erro': 'CEP não foi encontrado'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)