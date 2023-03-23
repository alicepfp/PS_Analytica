from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

hoje = datetime.today()
def calculaidade(aniversario, data=hoje):   
    
    str_nasc = str(aniversario)
    str_data = str(data)

    a = int(str_nasc[0:4])
    m = int(str_nasc[5:7])
    d = int(str_nasc[8:10])

    A = int(str_data[0:4])
    M = int(str_data[5:7])
    D = int(str_data[8:10])
    
    dias = (31 + (D - d)) if (D < d) else (D - d)

    meses = (12 + (M - m)) if (M < m) else (M - m)
    if (D < d):
        months-=1

    anos = (Y - y) if ((M - m) == 0) else ((Y - y) - 1)
    
    return anos


@app.route('/age', methods=['POST'])
def idade():
    if request.method == 'POST':
        dados_request = request.get_json(force=True)
        hoje = str(datetime.today())

        nome = None
        aniversario = None
        data = None

        if dados_request:
            if "nome" in dados_request:
                nome = dados_request["ome"]

            if "aniversario" in dados_request:
                aniversario = dados_request["aniversario"]

            if "data" in dados_request:
                data = dados_request["data"]
                if str(data) == str(hoje):
                    return 'Forneça outro dia futuro'
    
        idadehoje = calculaidade(aniversario)
        idadeoutro = calculaidade(aniversario, data)

        ano = data[0:4]
        mes = data[5:7]
        dia = data[8:10]

        formatado = dia + '/' + mes + '/' + ano
    
        frase = 'Olá, {}! Você tem {} anos e em {} você terá {} anos.'.format(nome, idadehoje, formatado, idadeoutro)

        data = {
            "quote": frase, 
            "ageNow": idadehoje,
            "ageThen": idadeoutro
                }
    
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)



