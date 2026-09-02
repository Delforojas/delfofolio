# Feature: Experiencia Laboral

## Descripción

La sección de experiencia laboral presenta trabajos previos o actuales con datos del cargo, empresa, ubicación, tipo de empleo y descripción.

## Evidencia en el código

- Ruta `experiencialaboral/` en `webpersonal/urls.py`
- Vista `experiencia_laboral` en `laboral/views.py`
- Modelo `ExperienciaLaboral` en `laboral/models.py`
- Plantilla `laboral/templates/laboral/laboral.html`

## Criterios de aceptación

- La ruta `/experiencialaboral/` renderiza la experiencia laboral.
- El modelo admite cargo, empresa, ubicación, tipo de empleo y descripción.
- Hay un campo para indicar si la experiencia es actual.
- La vista obtiene los registros con `ExperienciaLaboral.objects.all()`.

## Límite observado

No hay evidencia de filtros por fecha, empresa o categoría más allá de la consulta directa sobre el modelo.
