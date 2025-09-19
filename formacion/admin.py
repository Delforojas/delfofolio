# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Formar, FormacionAcademica

@admin.register(Formar)
class FormarAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")
    list_display = ("title", "plataforma", "instructor", "duracion", "fecha_finalizacion", "ver_certificado")
    list_filter = ("plataforma", "instructor", "fecha_finalizacion", "creado")
    search_fields = ("title", "plataforma", "instructor", "descripcion")
    date_hierarchy = "fecha_finalizacion"
    ordering = ("-creado",)

    def ver_certificado(self, obj):
        if obj.certificado:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;" />', obj.certificado.url)
        return "—"
    ver_certificado.short_description = "Certificado"

@admin.register(FormacionAcademica)
class FormacionAcademicaAdmin(admin.ModelAdmin):
    readonly_fields = ("creado", "actualizado")
    list_display = ("titulo", "institucion", "disciplina", "en_curso", "fecha_inicio", "fecha_fin", "ver_certificado")
    list_filter = ("en_curso", "institucion", "disciplina", "fecha_inicio", "fecha_fin")
    search_fields = ("titulo", "institucion", "disciplina", "nota")
    date_hierarchy = "fecha_inicio"
    ordering = ("-fecha_fin", "-fecha_inicio")

    def ver_certificado(self, obj):
        if obj.certificado:
            return format_html('<img src="{}" style="height:40px;border-radius:4px;" />', obj.certificado.url)
        return "—"
    ver_certificado.short_description = "Certificado"
