# Desarrollo, tests y despliegue

## Instalación local

```bash
git clone https://github.com/Delforojas/delfofolio.git
cd delfofolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

El código no importa `python-dotenv`, por lo que copiar `.env` no exporta variables por sí mismo. Hay que sustituir el valor ficticio de `DJANGO_SECRET_KEY` por una clave generada y exportar las variables antes de utilizar Django:

```bash
export DJANGO_SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Después:

```bash
python manage.py migrate
python manage.py runserver
```

La aplicación queda disponible en `http://127.0.0.1:8000/`.

## Tests y comprobaciones

Los tests de Django cubren páginas públicas, navegación, tecnologías, proyectos, dashboards, datasets, formación y experiencia laboral.

```bash
python manage.py test
python manage.py check
```

También se puede comprobar la colección de estáticos con:

```bash
python manage.py collectstatic --noinput
```

## Producción

Existe una versión desplegada en [https://delforojas.es](https://delforojas.es). La documentación y configuración del proyecto hacen referencia a PythonAnywhere y a un dominio personalizado.

El repositorio no especifica todos los detalles internos del servidor ni confirma una base de datos de producción distinta de la SQLite configurada por defecto. Esos valores deben definirse en el entorno de despliegue.
