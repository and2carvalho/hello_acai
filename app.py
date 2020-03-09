from flask import Flask, jsonify, request
from flask_cors import CORS
from conn import db
from model import Acai

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db_acai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = ''

db.init_app(app)
CORS(app, resources={r'/*': {'origins': '*'}})

dic_op = {
    "op_tam" : {
        "Pequeno (300ml)" : "Pequeno (300ml)",
        "Médio (500ml)" : "Médio (500ml)",
        "Grande (700ml)" : "Grande (700ml)"
        },
    "op_sabor" : {
        "Morango" : "Morango",
        "Banana" : "Banana",
        "Kiwi" : "Kiwi"
        },
    "op_adicional" : {
       "Granola" : "Granola",
        "Paçoca" : "Paçoca",
        "Leite Ninho" : "Leite Ninho"
        }
    }

@app.route('/pedido', methods=["POST", "GET"])
def pedidoAcai():
    tempo_preparo = 0
    valor_total = 0
    tamanho = None
    sabor = None
    adicional = None

    if request.method == "POST":
        post_data = request.get_json()
        tamanho = post_data["tamanho"]
        sabor = post_data["sabor"]
        adicional = post_data["adicional"]
        # diferencial tamanho
        if tamanho == "Pequeno (300ml)": # tamanho pequeno
            tempo_preparo += 5
            valor_total += 10
        elif tamanho == "Médio (500ml)": # tamanho medio
            tempo_preparo += 7
            valor_total += 13
        else:
            tempo_preparo += 10
            valor_total += 15
        # diferencial sabor
        if sabor == "Kiwi" : # sabor kiwi
            tempo_preparo += 5
        else:
            pass
        # diferencial adicional
        if adicional == "Paçoca": # adicional paçoca
            tempo_preparo += 3
            valor_total += 3
        elif adicional == "Leite Ninho": # adicional leite ninho
            valor_total += 3
        else:
            pass
        try:
            dic = {
                "tamanho" : tamanho,
                "sabor" : sabor,
                "adicional" : adicional,
                "tempo_preparo" : tempo_preparo,
                "valor_total" : valor_total
                }
            pedido = Acai(**dic)
            db.session.add(pedido)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify({"Status" : "Error"})

        return jsonify({
            "tamanho" : dic_op["op_tam"].get(tamanho),
            "sabor" : dic_op["op_sabor"].get(sabor),
            "adicional" : dic_op["op_adicional"].get(adicional),
            "tempo_preparo" : tempo_preparo,
            "valor_total" : valor_total,
            "id_pedido" : pedido.codigo
            })
    else:
        tempo_preparo = 0
        valor_total = 0
        return jsonify({
            "dic_op" : dic_op,
            "tempo_preparo" : tempo_preparo,
            "valor_total" : valor_total
            })



if __name__ == '__main__':
    app.run()