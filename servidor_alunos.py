from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello():
        print("rodei mesmo")
        return "Hello World!"


# no app,route, especificamos URL e verbo
@app.route("/nomes", methods=["GET"])
def hello2():
        return "Eder, Ana e outros"  # a funcao retorna uma string


dados = {"alunos": [
                   {"nome": "lucas", "id": 15},
                   {"nome": "cicero", "id": 29},
                  ],
        "professores": [
            {"nome":"Frida", "id": 24},
            {"nome":"Fernanda", "id": 32}
        ]}

'''atende em /alunos, verbo GET'''


@app.route("/alunos", methods=["GET"])
def alunos():
    return jsonify(dados['alunos'])
    'json ify = json ificar'
    "ele nao sabe retornar listas, mas sabe retornar strings"
    "entao, transforma a minha lista numa string json"


@app.route("/alunos/<int:nAluno>", methods=["GET", "DELETE", "PUT"])
def alunoPorId(nAluno):
    if request.method == "DELETE":
        for al in dados["alunos"]:
            if al['id'] == request.json['id']:
                dados["alunos"].remove(al)
        return jsonify(dados['alunos'])
    for item in dados['alunos']:
            if item["id"] == nAluno:
                if request.method == "GET":
                    return item
                if request.method == "PUT":
                    if request.json["nome"] == "":
                        return {'erro':'aluno sem nome'}, 400
                    item["nome"] = request.json["nome"]
                    return item    
    return {"erro": "aluno nao encontrado"}, 400
        
        

'''atende em /alunos, verbo POST'''
@app.route("/alunos", methods=["POST"])
def cria_aluno():
    dict = request.json #request.json representa um arquivo json enviado ao servidor
    if dict['nome'] == '':
        return {'erro':'aluno sem nome'}, 400
    for item in dados["alunos"]:
        if item['id'] == dict['id']:
            return {'erro':'id ja utilizada'}, 400
    # nosso servidor recebeu um arquivo e colocou nessa variavel
    dados['alunos'].append(dict)
    return jsonify(dados['alunos'])

@app.route("/reseta", methods=["POST"])
def resete():
    try:
        dados["alunos"].clear()
        dados["professores"].clear()
        return "sucesso"
    except:
        return "erro"


@app.route("/professores", methods=["GET"])
def professores():
    return jsonify(dados['professores'])
    'json ify = json ificar'
    "ele nao sabe retornar listas, mas sabe retornar strings"
    "entao, transforma a minha lista numa string json"


@app.route("/professores/<int:nProf>", methods=["GET", "DELETE", "PUT"])
def professorPorId(nProf):
    if request.method == "DELETE":
        for al in dados["professores"]:            
            if al['id'] == nProf:
                dados["professores"].remove(al)
        return jsonify(dados['professores'])
    for item in dados['professores']:
            if item["id"] == nProf:
                if request.method == "GET":
                    return item
                if request.method == "PUT":
                    if request.json["nome"] == "":
                        return {'erro':'professor sem nome'}, 400
                    item["nome"] = request.json["nome"]
                    return item    
    return {"erro": "professor nao encontrado"}, 400
        
        

'''atende em /alunos, verbo POST'''
@app.route("/professores", methods=["POST"])
def cria_professor():
    dict = request.json #request.json representa um arquivo json enviado ao servidor
    if dict['nome'] == '':
        return {'erro':'professor sem nome'}, 400
    for item in dados["professores"]:
        if item['id'] == dict['id']:
            return {'erro':'id ja utilizada'}, 400
    # nosso servidor recebeu um arquivo e colocou nessa variavel
    dados['professores'].append(dict)
    return jsonify(dados['professores'])


if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)
       
