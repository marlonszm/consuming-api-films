from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

usuarios = [
    {
        "login": "marlon",
        "senha": "12345"
    }
]

frutas = []

@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        login = request.form.get("login").lower()
        senha = request.form.get("senha")
        for usuario in usuarios:
            if usuario["login"] == login and usuario["senha"] == senha:
                return redirect(url_for("sobre"))
        
        return "Login ou usuário incorretos"
    return render_template("index.html")


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("adicionar"):
            frutas.append(request.form.get("adicionar"))
            return render_template("sobre.html", frutas=frutas)
    else:
        return render_template("sobre.html", frutas=frutas)

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
