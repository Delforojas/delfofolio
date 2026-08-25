# Plan de la feature: About / Contacto

## Implementación actual

La feature está implementada en la app `core`.

### Rutas

```python
path('about-me/', core_views.about, name="about"),
path('contact/', core_views.contact, name="contact"),
```

### Vistas

```python
def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")
```

### Plantillas

- `core/templates/core/about.html`
- `core/templates/core/contact.html`

Ambas aprovechan el layout común definido en `core/templates/core/base.html`.

## Dependencias

- `webpersonal/urls.py`
- `core/views.py`
- `core/templates/core/base.html`
- archivos estáticos asociados a estilo visual

## Verificación posible

Ejecutar el proyecto y comprobar que `/about-me/` y `/contact/` cargan las páginas correspondientes.
