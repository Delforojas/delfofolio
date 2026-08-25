# Feature: Portfolio

## Descripción

La sección de portafolio muestra una colección de proyectos, cada uno con título, descripción, imagen, fecha y enlace opcional.

## Evidencia en el código

- Ruta `portfolio/` en `webpersonal/urls.py`
- Vista `portfolio` en `portfolio/views.py`
- Modelo `Project` en `portfolio/models.py`
- Plantilla `portfolio/templates/portfolio/portfolio.html`

## Criterios de aceptación

- La ruta `/portfolio/` muestra todos los proyectos registrados.
- Cada proyecto incluye al menos: título, descripción, imagen y fecha de creación.
- Si existe un enlace, se muestra con un enlace externo.
- Si no hay imagen, la plantilla usa una imagen por defecto.
- Los datos se obtienen con `Project.objects.all()`.

## Límite observado

La funcionalidad depende de registros creados en la base de datos. No hay fixtures ni datos iniciales en el repositorio que documenten proyectos concretos.
