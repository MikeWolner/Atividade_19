from flask import Flask, request, jsonify

app = Flask(__name__)
produtos = [{'codigo': '1', 'nome': 'Cachorro quente', 'preco': 12.00},
            {'codigo': '2', 'nome': 'Sanduíche', 'preco': 23.89},
            {'codigo': '3', 'nome': 'Pastel', 'preco': 3.98},
            {'codigo': '4', 'nome': 'Refrigerante', 'preco': 5.72},
            {'codigo': '5', 'nome': 'Suco', 'preco': 4.35}]  

#Todos os produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    return jsonify({'produtos': produtos})

#Um produto
@app.route('/produtos/<string:codigo>', methods=['GET'])
def retornar_produto(codigo):
    resp = {'produto': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            resp = produto
    return jsonify(resp)

#Inserir novos itens
@app.route('/produtos/<string:nome>/<float:preco>', methods=['POST'])
def inserir_produto(codigo, nome, preco):
    produtos.append({'codigo': codigo, 'nome': nome, 'preco': preco})
    return jsonify({'codigo': codigo, 'nome':nome, 'preco':preco})

#Alterar produto todo
@app.route('/produtos/<string:codigo>/<string:nome>/<float(signed=True):preco>', methods=['PUT'])
def alterar_produto(codigo, nome, preco):
    resp = {'produto': '', 'nome': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['nome'] = nome
            produto['preco'] = preco
            resp = produto
    return jsonify(resp)

#Alterar nome do produto
@app.route('/produtos/<string:codigo>/<string:nome>', methods=['PATCH'])
def alterar_nome_do_produto(codigo, nome):
    resp = {'produto': '', 'nome': ''}
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['nome'] = nome
            resp = produto
    return jsonify(resp)

#alterar o preco
@app.route('/produtos/<string:codigo>/<float(signed=True):preco>', methods=['PATCH'])
def alterar_preço_do_produto(codigo, preco):
    resp = {'produto': '', 'preco': None}
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['preco'] = preco
            resp = produto
    return jsonify(resp)

#deletar produtos
@app.route('/produtos/<string:codigo>', methods=['DELETE'])
def remover_produto(codigo):
    for i, produto in enumerate(produtos):
        if produto['codigo'] == codigo:
            del produtos[i]
    return jsonify({'produtos': produtos})






if __name__ == '__main__':
    app.run(debug = True, port = 5000)
