#!/bin/bash

# Instala las dependencias de Python
pip install -r requirements.txt

# Recolecta los archivos estáticos de Django
python manage.py collectstatic --noinput --clear