# Feature: Datasets / Recursos

## Descripción

La sección de datasets muestra una colección de recursos con información general, imagen opcional, enlace a GitHub y archivo HTML asociado.

## Evidencia en el código

- Ruta `dataset/` en `webpersonal/urls.py`
- Vista `dataset` en `dataset/views.py`
- Modelo `Dataset` en `dataset/models.py`
- Plantilla `dataset/templates/dataset/dataset.html`

## Criterios de aceptación

- La ruta `/dataset/` renderiza la página de recursos.
- La vista obtiene todos los registros con `Dataset.objects.all()`.
- Cada elemento puede tener: título, descripción, imagen, enlace GitHub y archivo HTML.
- La plantilla recorre los registros para mostrarlos.

## Límite observado

No hay evidencia de un flujo de descarga o de un gestor de archivos más complejo que la representación de estos objetos en la interfaz.
