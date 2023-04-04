# :card_index_dividers: project-python3-django

> Template de Python 3 con Django

![alt](docs/img/python-django.png)

## :gear: Requisitos

* python 3
* virtualenv

## :tada: Uso

```bash
# Creacion del virtual env
virtualenv -p python3 env

# Activar el virtual env
. env/bin/activate

# Instalacion de los requerimientos
pip install -r requirements.txt

# Configurar la app
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser

# Levantar el server
python manage.py runserver
```

