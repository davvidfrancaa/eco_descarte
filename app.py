from flask import Flask, render_template, request
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

pontos = [
    {
        "nome": "Ecoponto Centro",
        "material": "eletronicos",
        "endereco": "Rua Central 100",
        "horario": "08:00 - 17:00",
        "mapa": "https://www.google.com/maps"
    },
    {
        "nome": "Ecoponto Norte",
        "material": "plastico",
        "endereco": "Av Norte 200",
        "horario": "09:00 - 18:00",
        "mapa": "https://www.google.com/maps"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/locais")
def locais():
    material = request.args.get("material")

    if material:
        lista = [p for p in pontos if p["material"] == material]
    else:
        lista = pontos

    return render_template("locais.html", pontos=lista)


@app.route("/coleta", methods=["GET","POST"])
def coleta():

    if request.method == "POST":

        nome = request.form["nome"]
        endereco = request.form["endereco"]
        item = request.form["item"]

        foto = request.files["foto"]

        if foto:
            caminho = os.path.join(app.config["UPLOAD_FOLDER"], foto.filename)
            foto.save(caminho)

        protocolo = str(uuid.uuid4())[:8]

        return render_template("protocolo.html", protocolo=protocolo)

    return render_template("coleta.html")


@app.route("/denuncia", methods=["GET","POST"])
def denuncia():

    if request.method == "POST":

        local = request.form["local"]
        descricao = request.form["descricao"]

        foto = request.files["foto"]

        if foto:
            caminho = os.path.join(app.config["UPLOAD_FOLDER"], foto.filename)
            foto.save(caminho)

        protocolo = str(uuid.uuid4())[:8]

        return render_template("protocolo.html", protocolo=protocolo)

    return render_template("denuncia.html")


if __name__ == "__main__":
    app.run(debug=True)