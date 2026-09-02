# Feature: About / Contacto

## Descripción

La app `core` contiene las páginas transversales de información personal y contacto. La navegación principal incluye enlaces a `about-me/` y `contact/`.

## Evidencia en el código

- Rutas en `webpersonal/urls.py`
- Vistas `about` y `contact` en `core/views.py`
- Plantillas `core/templates/core/about.html` y `core/templates/core/contact.html`

## Criterios de aceptación

- La ruta `/about-me/` renderiza una vista de descripción profesional o personal.
- La ruta `/contact/` renderiza una vista de contacto.
- Ambos usos se sirven desde `core/views.py` con `render()`.
- La navegación se reutiliza desde el layout base.

## Límite observado

No se ha identificado un formulario funcional real ni una lógica de envío de mensajes en el código actual.
