from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "clave_sistema_turistico"

usuarios = {
    "admin": "1234",
    "usuario": "12345"
}


@app.route("/", methods=["GET", "POST"])
def inicio_sesion():

    mensaje = ""

    if request.method == "POST":

        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]

        if usuario in usuarios and usuarios[usuario] == contrasena:

            session["usuario"] = usuario

            return redirect(url_for("inicio"))

        else:

            mensaje = "Usuario o contraseña incorrectos"

    return render_template(
        "inicio_sesion.html",
        mensaje=mensaje
    )


@app.route("/inicio")
def inicio():

    if "usuario" not in session:
        return redirect(url_for("inicio_sesion"))

    return render_template(
        "inicio.html",
        usuario=session["usuario"]
    )


@app.route("/cerrar_sesion")
def cerrar_sesion():

    session.clear()

    return redirect(url_for("inicio_sesion"))


if __name__ == "__main__":
    app.run(debug=True)
    