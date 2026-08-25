# Plan de la feature: Experiencia Laboral

## Implementación actual

### Modelo

`laboral/models.py` define `ExperienciaLaboral` con:

- `cargo`
- `tipo_empleo`
- `empresa`
- `ubicacion`
- `tipo_ubicacion`
- `certificado`
- `fecha_inicio`
- `fecha_fin`
- `actualmente`
- `descripcion`
- `creado`
- `actualizado`

### Vista

```python
def experiencia_laboral(request):
    laborales = ExperienciaLaboral.objects.all()
    return render(request, "laboral/laboral.html", {'laborales': laborales})
```

### Plantilla

`laboral/templates/laboral/laboral.html` itera sobre `laborales` para mostrar la experiencia laboral.

### Ruta

```python
path('experiencialaboral/', experiencia_laboral_views.experiencia_laboral, name='experiencialaboral')
```

## Dependencias

- `laboral/models.py`
- `laboral/views.py`
- `laboral/templates/laboral/laboral.html`
- `webpersonal/urls.py`

## Verificación posible

Crear registros de `ExperienciaLaboral` desde Django Admin y confirmar que se muestran en `/experiencialaboral/`.
