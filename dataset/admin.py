from django.contrib import admin
from .models import Dataset

class DatasetAdmin(admin.ModelAdmin):
    readonly_fields = ('creado',)  # si tienes el campo creado en el modelo

# Registro del modelo con configuración personalizada
admin.site.register(Dataset, DatasetAdmin)