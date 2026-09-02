# AGENTS.md

## 1) Propósito del proyecto

Este repositorio es un proyecto Django para una web personal / portafolio profesional. La aplicación presenta contenido de:

- portada o home
- acerca de
- portafolio de proyectos
- datasets o recursos
- formación (cursos y formación académica)
- experiencia laboral
- contacto

La evidencia del repositorio muestra que el objetivo principal es exponer información profesional y proyectos del autor, con contenido administrable mediante Django Admin y archivos multimedia (imágenes, certificados, archivos HTML).

## 2) Stack tecnológico

La tecnología del proyecto se infiere directamente de los archivos del repositorio:

- Python como lenguaje principal
- Django 5.1.7 en `requirements.txt`
- SQLite como base de datos por defecto (`db.sqlite3` y `DATABASES` en `webpersonal/settings.py`)
- Django Admin
- `django-ckeditor` para contenido enriquecido (`RichTextField` en `formacion/models.py`)
- `Pillow` para manejo de imágenes
- archivos estáticos y media con Django (`STATIC_URL`, `MEDIA_URL`, `STATIC_ROOT`, `MEDIA_ROOT`)
- Bootstrap, jQuery y Font Awesome en `core/static/core/vendor/...` para la UI
- Pylint y Black aparecen en configuración local de VS Code y dependencias

No se detecta un frontend basado en React, Vite, Angular, Vue, Node o TypeScript en este repositorio. La interfaz está construida con Django templates + assets estáticos.

## 3) Estructura de carpetas

```text
.
├── .gitignore
├── .vscode/
│   └── settings.json
├── AGENTS.md
├── db.sqlite3
├── manage.py
├── requirements.txt
├── media/
│   ├── certificados/
│   └── projects/
├── staticfiles/
│   └── ... archivos estáticos compilados
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── static/
│   │   └── core/
│   └── templates/
│       └── core/
├── dataset/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── dataset/
├── formacion/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── formacion/
├── laboral/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── laboral/
├── portfolio/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       └── portfolio/
├── webpersonal/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── ...
```

## 4) Arquitectura

El proyecto sigue la arquitectura típica de Django:

- `webpersonal/` es el proyecto principal y centraliza configuración global.
- Cada carpeta como `core`, `portfolio`, `formacion`, `laboral`, `dataset` es una app Django con responsabilidad específica.
- Cada app contiene:
  - `models.py`: definición de entidades persistentes
  - `views.py`: lógica de renderizado
  - `templates/...`: plantillas HTML
  - `migrations/`: historial de esquema de base de datos
- Las rutas públicas se definen en `webpersonal/urls.py` y apuntan a vistas de cada app.
- La capa de presentación se resuelve con plantillas Django (`extends`, `{% block %}`, `{% load static %}`) y un `base.html` compartido.
- El contenido estático se concentra en `core/static/core/...` y se sirve con `STATICFILES_DIRS`.
- El contenido de usuario multimedia se sirve desde `media/`.

Patrón observado:

- `core`: páginas transversales (`home`, `about`, `contact`)
- `portfolio`: proyectos propios
- `formacion`: cursos y formación académica
- `laboral`: experiencia laboral
- `dataset`: recursos / datasets / enlaces / archivos

## 5) Comandos para ejecutar el proyecto

Estos comandos se desprenden del propio proyecto Django y su configuración:

### Preparar entorno

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Migraciones y arranque

```bash
python manage.py migrate
python manage.py runserver
```

### Administración

```bash
python manage.py createsuperuser
python manage.py shell
```

### Recopilar archivos estáticos

```bash
python manage.py collectstatic --noinput
```

Esto está alineado con la configuración de `STATIC_ROOT` en `webpersonal/settings.py`.

## 6) Comandos de tests, lint y build

### Tests

El repositorio no incluye un framework de tests específico distinto de Django. La convención Django por defecto es:

```bash
python manage.py test
```

Se detectan archivos `tests.py` vacíos en todas las apps, por lo que no hay pruebas implementadas todavía en el código actual.

### Lint

Se detecta `pylint` en `requirements.txt` y en `.vscode/settings.json` la configuración de linting de Python. La forma más probable y compatible con el proyecto es:

```bash
pylint core portfolio formacion laboral dataset
```

o, si se quiere apuntar a un archivo concreto:

```bash
pylint core/views.py
```

No se detecta una configuración de `pylintrc` o `pyproject.toml` específica del proyecto, así que el lint parece depender del entorno local y de la configuración por defecto de Pylint.

### Build

No se detecta sistema de build JavaScript o frontend (no hay `package.json`, `webpack.config.js`, `vite.config.*`, `tsconfig.json`, etc.).

La operación de compilación más cercana en este proyecto Django es:

```bash
python manage.py collectstatic --noinput
```

Esto genera la carpeta `staticfiles/` para archivos estáticos. Se trata de una preparación de despliegue/servicio y no de un build de frontend moderno.

## 7) Convenciones detectadas

Convenciones observadas en el repositorio:

- Uso de apps Django con nombres y estructura estándar (`models.py`, `views.py`, `templates/...`, `apps.py`).
- Nombres de modelos y campos en español, con `verbose_name` y `help_text` en varios modelos.
- Uso de `auto_now_add` y `auto_now` para timestamps de creación y edición.
- Plantillas con herencia: `extends 'core/base.html'`.
- Archivos estáticos bajo `static/` por app y cargados con `{% load static %}`.
- Rutas públicas definidas en `webpersonal/urls.py` con `path()`.
- Estructura de contenido orientada a sitio personal/portfolio y no a API REST.
- URLs del tipo `route/` y nombres de reversión como `home`, `about`, `portfolio`, `formacion`, etc.
- Uso de `ImageField` y `FileField` para contenido administrativo.
- `DEBUG = False` en settings, con `ALLOWED_HOSTS` configurado específicamente para alojamiento en PythonAnywhere.

Convenciones no confirmadas o no presentes:

- No se han encontrado tests reales ni configuración de CI/CD.
- No se ha detectado un sistema de linting específico del proyecto más allá de Pylint.
- No se ha detectado un build pipeline de frontend ni un gestor de dependencias JS.

## 8) Flujo de trabajo

Workflow típico para este proyecto:

1. Crear y activar un entorno virtual.
2. Instalar dependencias con `pip install -r requirements.txt`.
3. Ejecutar migraciones con `python manage.py migrate`.
4. Iniciar la app con `python manage.py runserver`.
5. Administrar el contenido en Django Admin (`/admin/`).
6. Subir imágenes o certificados en `media/` a través del admin o modelos.
7. Mantener las plantillas y rutas alineadas con los nombres de URL (`name='home'`, etc.).
8. Recolectar static files si se prepara despliegue: `python manage.py collectstatic --noinput`.

Este proyecto parece diseñado como una web de contenido más bien que como una API, por lo que el flujo de trabajo principal es administrativo y de edición visual mediante plantillas.

## 9) Reglas que un agente debe respetar al modificar el código

1. No inventar tecnología ni infraestructura que no exista en el repositorio.
2. Mantener la arquitectura Django monolítica actual: apps por dominio, plantillas, modelos y vistas separados.
3. Si se modifica una ruta pública, revisar y actualizar `webpersonal/urls.py` y las plantillas que la consumen.
4. Si se añade o cambia un modelo, considerar la necesidad de crear migraciones con Django.
5. Mantener la convención de nombres en español cuando se trabaje con `verbose_name`, `help_text` y textos de UI.
6. No editar `staticfiles/` manualmente si esos archivos son generados por `collectstatic`; preferir modificar archivos fuente bajo `core/static/...`.
7. No asumir API REST ni frontend SPA; la app usa templates Django.
8. Retener la configuración existente de `STATIC_URL`, `MEDIA_URL` y rutas de archivos estáticos.
9. Preservar la compatibilidad con `Django 5.1.7` y las dependencias actuales de `requirements.txt`.
10. Probar cambios relevantes con `python manage.py check` o `python manage.py test` cuando corresponda.
11. Si no se puede inferir un comportamiento o una convención, documentarlo y no asumirlo en el código.
12. Cuidar el contenido multimedia y no borrar archivos generados sin justificarlo.

## 10) Observaciones y límites del repositorio

Se pueden determinar estos puntos con bastante certeza:

- Es un proyecto Django de web personal.
- Usa apps separadas por contenido.
- Tiene base de datos SQLite.
- Usa plantillas Django con assets estáticos.

No se puede afirmar con certeza, a partir del repositorio, lo siguiente:

- no hay README ni documentación de despliegue detallada
- no hay CI/CD pipeline definido
- no hay pruebas de negocio ni cobertura de tests configurada
- no hay configuración de build frontend ni npm/yarn
- no hay entorno de producción concreto documentado más allá de `ALLOWED_HOSTS` apuntando a PythonAnywhere

En resumen, este repositorio es un sitio personal Django monolítico, orientado a contenido y administración, con una organización clara por apps y una capa visual basada en templates y assets estáticos.
