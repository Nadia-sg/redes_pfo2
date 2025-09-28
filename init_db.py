# init_db.py
import sqlite3

DB_PATH = "tareas.db"

def crear_tablas():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Tabla de usuarios: guardamos el hash de la contraseña (no la contraseña en texto plano)
    cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    ''')


    cur.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            titulo TEXT NOT NULL,
            descripcion TEXT,
            creada_en TEXT NOT NULL,
            FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tablas()
    print("Base de datos inicializada en tareas.db")
