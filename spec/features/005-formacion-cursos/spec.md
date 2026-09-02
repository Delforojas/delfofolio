# Feature: Formación / Cursos

## Descripción

La sección de formación incluye cursos con datos como título, plataforma, instructor, duración, descripción enriquecida, enlace, certificado y fecha de finalización.

## Evidencia en el código

- Ruta `formacion/` en `webpersonal/urls.py`
- Vista `formacion` en `formacion/views.py`
- Modelo `Formar` en `formacion/models.py`
- Plantilla `formacion/templates/formacion/formacion.html`

## Criterios de aceptación

- La ruta `/formacion/` presenta los cursos registrados.
- Cada curso contiene al menos: título, plataforma, fecha de finalización y descripción.
- La descripción usa `RichTextField` de django-ckeditor.
- El modelo incluye imagen de certificado y enlace opcional.
- La vista obtiene los registros con `Formar.objects.all()`.

## Límite observado

No se ha detectado flujo de filtrado ni edición por front-end aparte de la renderización desde la base de datos.
