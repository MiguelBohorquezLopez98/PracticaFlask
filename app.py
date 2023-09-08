from flask import Flask, redirect, url_for, request, render_template, \
    flash, session
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "so-secret"

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/contacto/")
def contact():
    return """
    <h1 style="font-size: 64px; color:blue;">Contacto</h1>
    """

@app.route("/nosotros/")
def about():
    return """
    <h1 style="font-size: 64px; color:blue;">Nosotros</h1>
    """


@app.route("/login/", methods=["GET", "POST"])
def login():
    print(request.get_json())
    print(request.json)
    print(request.args["greeting"])  #error 400
    print(request.args.get("greeting")) #none
    return "Login"



    # form = LoginForm()
    # if form.validate_on_submit() and request.method == "POST":
    #     username = request.form["username"]
    #     password = request.form["password"]
    #     if username and password:
    #         session["username"] = username
    #         return redirect(url_for("dashboard", name=username))
    #     flash("Por favor ingresa correctamente tus datos.", "error")
    # return render_template("login.html", form = form)

@app.route("/profile/<name>/")    
@app.route("/profile/")
def dashboard(name=None):
    if name is not None:
        flash(f"Bienvenido(a) {name}", "success")
        return render_template("dashboard.html", username=name)
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))