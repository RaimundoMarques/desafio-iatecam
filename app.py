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

#Criar uma api para:
# - Consultar todos
@app.route('/livros')
def obter_livros():
    return jsonify(livros)

# - Consultar por id
# - Editar 
# - Ecluir
app.run(port=5000, host='localhost', debug=True)