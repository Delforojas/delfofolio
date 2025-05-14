from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Formar(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    plataforma = models.CharField(max_length=100, verbose_name="Plataforma", help_text="Ej. Udemy, Coursera, edX...")
    instructor = models.CharField(max_length=100, verbose_name="Instructor", blank=True, null=True)
    duracion = models.PositiveIntegerField(verbose_name="Duración (horas)", blank=True, null=True)
    descripcion = RichTextField(verbose_name="Descripción")
    enlace = models.URLField(verbose_name="Enlace al curso", blank=True, null=True)
    certificado = models.ImageField(upload_to="certificados", verbose_name="Certificado", blank=True, null=True)
    fecha_finalizacion = models.DateField(verbose_name="Fecha de finalización")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "formacion"
        verbose_name_plural = "formaciones"
        ordering = ["-creado"]
    def __str__(self):
        return self.title

class FormacionAcademica(models.Model):
    institucion = models.CharField(max_length=150, verbose_name="Institución educativa")
    titulo = models.CharField(max_length=200, verbose_name="Título")
    disciplina = models.CharField(max_length=150, verbose_name="Disciplina académica", blank=True, null=True)
    certificado = models.ImageField(upload_to="certificados", verbose_name="Certificado", blank=True, null=True)
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización", blank=True, null=True)
    en_curso = models.BooleanField(default=False, verbose_name="¿Actualmente cursando?")
    
    nota = models.CharField(max_length=50, verbose_name="Nota", blank=True, null=True)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "formación académica"
        verbose_name_plural = "formaciones académicas"
        ordering = ["-fecha_fin", "-fecha_inicio"]

    def __str__(self):
        return f"{self.titulo} en {self.institucion}"
    