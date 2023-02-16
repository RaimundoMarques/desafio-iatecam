from flask import Flask, jsonify, request
from bd import Livros

app = Flask(__name__)

# - Consultar todos


@app.get('/')
def obter_livros():
    return jsonify(Livros)

# Criar uma api para:


# - Consultar por id
@app.get('/livros/<int:id>')
def obter_livros_id(id):
    for livro in Livros:
        if livro.get('id') == id:
            return jsonify(livro)


# - Editar
@app.put('/livros/<int:id>')
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(Livros):
        if livro.get('id') == id:
            Livros[indice].update(livro_alterado)
            return jsonify(Livros[indice])


# - Criar
@app.post('/livros')
def criar_livro():
    novo_livro = request.get_json()
    Livros.append(novo_livro)
    return jsonify(Livros)


# - Excluir
@app.delete('/livros/<int:id>')
def excluir_livro(id):
    for indice, livro in enumerate(Livros):
        if livro.get('id') == id:
            del Livros[indice]

    return jsonify(Livros)


app.run(port=5001, host='localhost', debug=True)
