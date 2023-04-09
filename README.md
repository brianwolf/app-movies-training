# :card_index_dividers: app-movies-training

> App de peliculas hecha como medio de aprendizaje para Jr en python

![alt](docs/img/tmdb.png)

## :gear: Requisitos

* python 3

## :tada: Uso

```bash
# Creacion del virtual env
python3 -m venv env

# Activar el virtual env
. env/bin/activate

# Instalacion de los requerimientos
pip install -r requirements.txt

# Configurar la app por primera vez
python manage.py migrate

# Levantar el server
python manage.py runserver
```

## Themoviedb

El proyecto hace uso de la API de la pagina [themoviedb](https://www.themoviedb.org/), la documentación de la API esta [aquí](https://developers.themoviedb.org/3/getting-started/introduction)

**api_key** = 4294d227a0bf641e389362f06c10279f

### Ejemplo de una llamada rest

<https://api.themoviedb.org/3/movie/550?api_key=4294d227a0bf641e389362f06c10279f>
