from flask import Flask, jsonify, request
app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos Anéis - A Sociedade do Anel',
        'author': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'O senhor dos Anéis - As Duas Torres',
        'author': 'J.R.R Tolkien'
    },
    {
        'id': 3,
        'titulo': 'O senhor dos Anéis - O Retorno do Rei',
        'author': 'J.R.R Tolkien'
    },
]

# Criar uma api para:
# - Consultar todos


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# - Consultar por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# - Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# - Criar


@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

# - Excluir


def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
