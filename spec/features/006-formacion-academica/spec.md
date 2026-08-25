# Feature: Formación Académica

## Descripción

La sección de formación académica presenta estudios y títulos obtenidos o en curso, con datos sobre la institución, disciplina, fechas, nota y certificado.

## Evidencia en el código

- Ruta `experiencia/` en `webpersonal/urls.py`
- Vista `experiencia` en `formacion/views.py`
- Modelo `FormacionAcademica` en `formacion/models.py`
- Plantilla `formacion/templates/formacion/experiencia.html`

## Criterios de aceptación

- La ruta `/experiencia/` renderiza la formación académica.
- Cada elemento incluye institución, título, fechas y posibilidad de estar en curso.
- El modelo admite certificado y nota opcional.
- La vista obtiene los registros con `FormacionAcademica.objects.all()`.

## Límite observado

No se detecta un flujo de comparación, filtro o ordenación más avanzada que la simple consulta por base de datos.
