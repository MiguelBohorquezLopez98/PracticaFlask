## Crear entorno virtual

python3 -m venv .venv

## Activar entorno virtual
. venv/bin/activate

## Instalar Flask
pip install Flask

## Instalar dependendias
pip install python-dotenv
pip install -U flask_wtf

## Correr programa
En el archivo .env asegurarse de tener lo siguientes:
```FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1```
para luego usar el comando flask run y poder correr la pagina web

