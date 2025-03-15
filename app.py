from flask import Flask, request, jsonify, render_template
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite el acceso desde el frontend

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Endpoint para buscar persona por cédula
@app.route("/buscar", methods=["GET"])
def buscar_persona():
    cedula = request.args.get("cedula")
    conn = sqlite3.connect("database/personas.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM personas WHERE cedula = ?", (cedula,))
    persona = cursor.fetchone()
    conn.close()

    if persona:
        return jsonify({"cedula": persona[0], "nombre": persona[1], "apellido": persona[2], "edad": persona[3]})
    else:
        return jsonify({"error": "Persona no encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
