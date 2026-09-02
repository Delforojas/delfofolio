# Plan de la feature: Home / Portada

## Implementación actual

La feature está implementada en la app `core`.

### Ruta

```python
path('', core_views.home, name="home")
```

### Vista

`core/views.py` define:

```python
def home(request):
    return render(request, "core/home.html")
```

### Plantilla

`core/templates/core/home.html` extiende `core/base.html` y añade el contenido de la portada y scripts específicos de fondo visual.

### Elementos visuales

- layout base con navegación general
- cabecera con texto de presentación
- scripts JavaScript para renderizar fondo visual

## Dependencias

- `core/templates/core/base.html`
- `core/static/core/...` para CSS y JS asociados
- `webpersonal/urls.py` para enlazar la ruta

## Verificación posible

Para verificar la feature: arrancar el proyecto, navegar a `/` y comprobar que se carga la portada con el contenido principal del autor.
