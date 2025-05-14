from django.contrib import admin
from .models import ExperienciaLaboral

class ExperienciaLaboralAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

# ✅ REGISTRO CORRECTO
admin.site.register(ExperienciaLaboral, ExperienciaLaboralAdmin)