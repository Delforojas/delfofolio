# Plan de la feature: Formación Académica

## Implementación actual

### Modelo

`formacion/models.py` define `FormacionAcademica` con:

- `institucion`
- `titulo`
- `disciplina`
- `certificado`
- `fecha_inicio`
- `fecha_fin`
- `en_curso`
- `nota`
- `creado`
- `actualizado`

### Vista

```python
def experiencia(request):
    formaciones = FormacionAcademica.objects.all()
    return render(request, "formacion/experiencia.html", {'formaciones': formaciones})
```

### Plantilla

`formacion/templates/formacion/experiencia.html` itera sobre `formaciones` para mostrar la información.

### Ruta

```python
path('experiencia/', experiencia_academica_views.experiencia, name='experiencia')
```

## Dependencias

- `formacion/models.py`
- `formacion/views.py`
- `formacion/templates/formacion/experiencia.html`
- `webpersonal/urls.py`

## Verificación posible

Crear registros de `FormacionAcademica` en Django Admin y confirmar que se muestran en `/experiencia/`.
