# Plan de la feature: Datasets / Recursos

## Implementación actual

### Modelo

`dataset/models.py` define `Dataset` con:

- `titulo`
- `descripcion`
- `imagen`
- `github_url`
- `archivo_html`
- `creado`

### Vista

```python
def dataset(request):
    datasets = Dataset.objects.all()
    return render(request, "dataset/dataset.html", {'datasets': datasets})
```

### Plantilla

`dataset/templates/dataset/dataset.html` itera sobre `datasets` y muestra cada recurso con su contenido.

### Ruta

```python
path('dataset/', dataset_views.dataset, name='dataset')
```

## Dependencias

- `dataset/models.py`
- `dataset/views.py`
- `dataset/templates/dataset/dataset.html`
- `webpersonal/urls.py`

## Verificación posible

Crear registros de `Dataset` desde Django Admin y comprobar que aparecen en `/dataset/`.
