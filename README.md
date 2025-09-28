
# Sistema de Gestión de Tareas (PFO2)

## a) Descripción del proyecto

API en Python con Flask + SQLite que permite:
- Registrar usuarios con contraseñas hasheadas
- Iniciar sesión
- Ver un HTML de bienvenida

## b) Requisitos
- Python 3.10 o superior
- Librerías: Flask, Werkzeug

## c) Instalación y ejecución
### Crear entorno virtual
python -m venv venv
### Activar venv
### Windows
venv\Scripts\activate
### Linux/Mac
source venv/bin/activate

### Instalar dependencias
pip install Flask Werkzeug

### Inicializar la base de datos
python init_db.py

### Ejecutar servidor
python server.py

## d) Cómo probar

Registro: POST a /registro con JSON {"usuario":"Sol", "contrasena":"123456"}

Login: POST a /login con JSON {"usuario":"Sol", "contrasena":"123456"}

HTML de bienvenida: GET a /tareas desde navegador

## Capturas de pantalla

### Registro de usuario
![Registro](imagenes/Prueba-registro.png)

### Login exitoso
![Login](imagenes/Prueba-login.png)

### HTML de bienvenida
![Bienvenida](imagenes/Prueba-tareas-html.png)

### DB Browser
![Base de Datos](imagenes/BaseDatos_dbBrowser.png)

## Respuestas Conceptuales de PFO2:
### ¿Por qué hashear contraseñas?</h3>
Nunca guardamos contraseñas en texto plano por seguridad.<br>
Si la base se filtra, un atacante no puede ver las contraseñas reales.<br>
Hash + salt (como hace generate_password_hash) hace que cada contraseña<br> 
se almacene de forma única y segura
### Ventajas de usar SQLite en este proyecto
Es Ligero y fácil de instalar (no requiere servidor adicional).<br>
Ideal para proyectos chicos o prácticas de laboratorio.<br>
Se guarda en un solo archivo (tareas.db), fácil de versionar o mover.