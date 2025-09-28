from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import render_template_string

app = Flask(__name__)
DB_PATH = "tareas.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

@app.route("/registro", methods=["POST"])
def registro():
    """
    Endpoint para registrar un usuario.
    Recibe JSON: {"usuario": "nombre", "contraseña": "1234"}
    Guarda el usuario con la contraseña hasheada.
    """
    data = request.get_json() or {}
    usuario = data.get("usuario")
    contrasena = data.get("contrasena") or data.get("contrasena")

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan 'usuario' o 'contraseña'"}), 400

    # Hasheamos la contraseña antes de guardar 
    pw_hash = generate_password_hash(contrasena)

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)", (usuario, pw_hash))
        conn.commit()
        conn.close()
        return jsonify({"mensaje": "Usuario registrado correctamente"}), 201
    except sqlite3.IntegrityError:
        # Usuario ya existe (clave primaria duplicada)
        return jsonify({"error": "El usuario ya existe"}), 409
    except Exception as e:
        return jsonify({"error": f"Error al acceder a la base de datos: {e}"}), 500


@app.route("/login", methods=["POST"])
def login():
    """
    Endpoint para iniciar sesión.
    Recibe JSON: {"usuario": "Sol", "contrasena": "123456"}
    Compara la contraseña con el hash almacenado en la base.
    """
    data = request.get_json() or {}
    usuario = data.get("usuario")
    contrasena = data.get("contrasena")

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan 'usuario' o 'contrasena'"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT password_hash FROM usuarios WHERE usuario = ?", (usuario,))
        fila = cur.fetchone()
        conn.close()

        if fila and check_password_hash(fila[0], contrasena):
            return jsonify({"mensaje": f"Bienvenido {usuario}!"})
        else:
            return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

    except Exception as e:
        return jsonify({"error": f"Error al acceder a la base de datos: {e}"}), 500
    
@app.route("/tareas", methods=["GET"])
def tareas():
    """
    Endpoint que devuelve un HTML de bienvenida.
    """
    html = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Bienvenido</title>
    </head>
    <body>
        <h1>¡Bienvenido al sistema de gestión de tareas!</h1>
        <p>Desde aquí podrás ver tus tareas.</p>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True, port=5000)



