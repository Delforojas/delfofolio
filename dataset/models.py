from django.db import models

class Dataset(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(
        upload_to="certificados",
        verbose_name="Imagen del certificado (JPG/PNG)",
        blank=True,
        null=True
    )
    github_url = models.URLField(
        max_length=300,
        verbose_name="Enlace a GitHub",
        blank=True,
        null=True,
        help_text="URL del repositorio en GitHub (ej. https://github.com/usuario/proyecto)"
    )
    archivo_html = models.FileField(
        upload_to="certificados",
        verbose_name="Archivo HTML del certificado",
        blank=True,
        null=True
    )
    
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de subida")

    class Meta:
        verbose_name = "dataset"
        verbose_name_plural = "datasets"
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo