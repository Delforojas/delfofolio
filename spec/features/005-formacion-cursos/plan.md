# Plan de la feature: Formación / Cursos

## Implementación actual

### Modelo

`formacion/models.py` define `Formar` con:

- `title`
- `plataforma`
- `instructor`
- `duracion`
- `descripcion` (`RichTextField`)
- `enlace`
- `certificado`
- `fecha_finalizacion`
- `creado`
- `actualizado`

### Vista

```python
def formacion(request):
    formars = Formar.objects.all()
    return render(request, "formacion/formacion.html", {'formars': formars})
```

### Plantilla

`formacion/templates/formacion/formacion.html` itera sobre `formars` para mostrar la información de cursos.

### Ruta

```python
path('formacion/', formacion_views.formacion, name="formacion")
```

## Dependencias

- `formacion/models.py`
- `formacion/views.py`
- `formacion/templates/formacion/formacion.html`
- `webpersonal/urls.py`
- `django-ckeditor`

## Verificación posible

Se pueden crear registros de `Formar` desde Django Admin y comprobar que se muestran en la ruta `/formacion/`.
