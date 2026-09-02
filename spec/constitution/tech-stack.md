# Stack tecnológico

## Tecnologías utilizadas realmente

La información de este documento se extrae de los archivos del repositorio y de la configuración del proyecto actual.

### Lenguaje principal

- Python

### Framework principal

- Django 5.1.7, según `requirements.txt`

### Base de datos

- SQLite, configurado en `webpersonal/settings.py`

### Administración

- Django Admin

### Dependencias observadas

Según `requirements.txt`:

- Django==5.1.7
- django-ckeditor==6.7.2
- Pillow==11.1.0
- pylint==3.3.6
- pylint-django==2.6.1
- django-js-asset==3.1.2

## Arquitectura

La arquitectura detectada es la de un proyecto Django monolítico con varias apps por dominio.

### Proyecto principal

- `webpersonal/`: configuración global del proyecto
  - `settings.py`
  - `urls.py`
  - `asgi.py`
  - `wsgi.py`

### Apps del dominio

- `core/`: vistas y plantillas transversales (`home`, `about`, `contact`)
- `portfolio/`: proyectos del portafolio
- `formacion/`: cursos y formación académica
- `laboral/`: experiencia laboral
- `dataset/`: datasets o recursos

Cada app suele incluir:

- `models.py`
- `views.py`
- `templates/`
- `migrations/`
- `admin.py`
- `apps.py`

## Estructura del proyecto

```text
.
├── .gitignore
├── .vscode/
├── AGENTS.md
├── db.sqlite3
├── manage.py
├── requirements.txt
├── media/
├── staticfiles/
├── core/
├── dataset/
├── formacion/
├── laboral/
├── portfolio/
├── webpersonal/
└── ...
```

## Presentación y assets

La capa visual se implementa con:

- templates de Django
- archivos estáticos bajo `core/static/core/...`
- Bootstrap
- jQuery
- Font Awesome

Se observa uso de `STATICFILES_DIRS` y `STATIC_ROOT` en `webpersonal/settings.py`.

## Multimedia

El proyecto gestiona almacenamiento de contenido de usuario en:

- `media/`
- `MEDIA_URL = '/media/'`
- `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

Los modelos usan `ImageField` y `FileField` para contenido como certificados, proyectos y datasets.

## Convenciones detectadas

- Modelos y campos en español
- `verbose_name` y `help_text` en varios modelos
- uso de `auto_now_add` y `auto_now`
- plantillas con herencia (`extends`) y bloques (`{% block %}`)
- rutas públicas con `path()` en `webpersonal/urls.py`
- contenido orientado a sitio personal y portfolio, no a API REST
- uso de `RichTextField` para contenido enriquecido en la formación

## Comandos de ejecución

Los comandos observables y compatibles con la configuración del proyecto son:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Comandos de administración

```bash
python manage.py createsuperuser
python manage.py shell
```

## Comandos de tests, lint y build

### Tests

La convención estándar de Django es:

```bash
python manage.py test
```

El repositorio tiene archivos `tests.py` vacíos en todas las apps, por lo que no hay pruebas implementadas que puedan documentarse como funcionalidad real.

### Lint

Se observa `pylint` en `requirements.txt` y configuración local de VS Code. Se puede ejecutar:

```bash
pylint core portfolio formacion laboral dataset
```

No hay evidencia de una configuración de lint específica del proyecto, así que este sería el uso más compatible con la infraestructura observada.

### Build

No se detecta un sistema de build de frontend como:

- `package.json`
- `vite.config.*`
- `webpack.config.js`
- `tsconfig.json`

La operación más cercana del proyecto es la colección de archivos estáticos:

```bash
python manage.py collectstatic --noinput
```

## Restricciones técnicas

- El proyecto está orientado a Django y plantillas HTML; no se observa SPA ni frontend JS moderno.
- La base de datos es SQLite por defecto y no se ha detectado configuración de PostgreSQL u otra base.
- El proyecto tiene `DEBUG = False` y `ALLOWED_HOSTS` específico para PythonAnywhere.
- No hay evidencia de CI/CD ni pipeline de despliegue documentado.
- No se ha detectado README de despliegue o arquitectura más detallada más allá del propio código.
