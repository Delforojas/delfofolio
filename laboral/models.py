from django.db import models

# Create your models here.
from django.db import models

class ExperienciaLaboral(models.Model):
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    tipo_empleo = models.CharField(max_length=100, verbose_name="Tipo de empleo")  # Ej. Jornada completa, Media jornada...
    empresa = models.CharField(max_length=100, verbose_name="Empresa u organización")
    ubicacion = models.CharField(max_length=100, verbose_name="Ubicación", blank=True, null=True)
    tipo_ubicacion = models.CharField(max_length=100, verbose_name="Tipo de ubicación", blank=True, null=True)  # Ej. Presencial, Remoto...
    certificado = models.ImageField(upload_to="certificados", verbose_name="Certificado", blank=True, null=True)
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización", blank=True, null=True)
    actualmente = models.BooleanField(default=False, verbose_name="Actualmente tengo este cargo")

    descripcion = models.TextField(verbose_name="Descripción", max_length=2000)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "experiencia laboral"
        verbose_name_plural = "experiencias laborales"
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return f"{self.cargo} en {self.empresa}"