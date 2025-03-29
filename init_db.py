import sqlite3
import json

# Conectar a la BD
conn = sqlite3.connect("database/personas.db")
cursor = conn.cursor()

# Crear la tabla con la columna foto
cursor.execute('''
    CREATE TABLE IF NOT EXISTS personas (
        cedula TEXT PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        genero TEXT,
        Fecha_Nacimiento TEXT,
        cargo TEXT,
        edad INTEGER,
        foto TEXT
    )
''')

# Cargar datos desde JSON
with open("database/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for persona in data:
    cursor.execute(
        "INSERT OR IGNORE INTO personas VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
        (persona["cedula"], persona["nombre"], persona["apellido"], persona["genero"],
         persona["Fecha_Nacimiento"], persona["cargo"], persona["edad"], persona["foto"])
    )

conn.commit()
conn.close()
