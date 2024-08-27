from flask import Flask, render_template, request, url_for, redirect
import urllib.request, json

app = Flask(__name__)

usuarios = [
    {
        "login": "marlon",
        "senha": "12345"
    }
]

clientes = [

]

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


@app.route('/filmes/<propiedade>', methods=['GET'])
def filmes(propiedade):
    if propiedade == "populares":
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=71449df069c07d2ed4c33c80027dd880"
    elif propiedade == "kids":
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=71449df069c07d2ed4c33c80027dd880"
    elif propiedade == "2010":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=71449df069c07d2ed4c33c80027dd880"
    elif propiedade == "drama":
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&api_key=71449df069c07d2ed4c33c80027dd880"
    elif propiedade == "tom_cruise":
        url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=71449df069c07d2ed4c33c80027dd880"
    else:
        return "Invalid property specified.", 400
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes=jsondata['results'])
if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)
