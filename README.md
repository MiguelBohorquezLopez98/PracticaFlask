# Crear entorno virtual

python3 -m venv .venv

# Activar entorno virtual
. venv/bin/activate

# Instalar Flask
pip install Flask

# Instalar dependendias
pip install python-dotenv
pip install -U flask_wtf

# Correr programa
En el archivo .env configurar FLASK_APP=app.py para luego usar el comando flask run

