# Plan de la feature: Portfolio

## Implementación actual

La feature se implementa con los siguientes bloques:

### Modelo

`portfolio/models.py` define `Project` con:

- `title`
- `description`
- `image`
- `link`
- `created`
- `updated`

### Vista

```python
def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects': projects})
```

### Plantilla

`portfolio/templates/portfolio/portfolio.html` itera sobre `projects` y muestra cada proyecto en una fila con imagen, título, descripción, enlace y fecha.

### Ruta

```python
path('portfolio/', portfolio_views.portfolio, name="portfolio")
```

## Dependencias

- `portfolio/models.py`
- `portfolio/views.py`
- `portfolio/templates/portfolio/portfolio.html`
- `webpersonal/urls.py`
- `core/templates/core/base.html`

## Verificación posible

1. Crear o registrar proyectos desde Django Admin.
2. Ejecutar la aplicación.
3. Visitar `/portfolio/`.
4. Confirmar que los proyectos aparecen en la plantilla.
