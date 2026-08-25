from django.db import models


class Project(models.Model):
    class Category(models.TextChoices):
        GENERAL = "general", "Proyecto"
        POWER_BI = "power_bi", "Power BI"

    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.GENERAL,
        verbose_name="Tipo",
    )
    technologies = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="Tecnologías",
    )
    link = models.URLField(
        max_length=500,
        verbose_name="Dirección web",
        null=True,
        blank=True,
    )
    github_link = models.URLField(
        max_length=500,
        verbose_name="Repositorio de GitHub",
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
