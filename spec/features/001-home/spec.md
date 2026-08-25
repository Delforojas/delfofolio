# Feature: Home / Portada

## Descripción

La página de inicio del sitio personal presenta la portada del autor con una presentación breve y visual. Se trata de la primera vista que se renderiza en la raíz del sitio.

## Evidencia en el código

- Ruta principal en `webpersonal/urls.py`
- Vista `home` en `core/views.py`
- Plantilla `core/templates/core/home.html`
- Base layout `core/templates/core/base.html`

## Criterios de aceptación

- Al entrar a la URL `/` se renderiza la portada.
- La plantilla usa `core/base.html` como layout base.
- La vista devuelve una respuesta renderizada con `render(request, "core/home.html")`.
- La página incluye contenido visual y texto de presentación del autor.

## Límite observado

No hay pruebas automatizadas que validen esta feature, y no se documenta un CMS específico para contenido de portada fuera del template y el contenido estático.
