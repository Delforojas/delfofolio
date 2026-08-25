from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import FormacionAcademica, Formar


class FormacionPageTests(TestCase):
    def test_courses_empty_state_and_shared_layout(self):
        response = self.client.get(reverse("formacion"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No se han registrado cursos todavía.")
        self.assertContains(response, "page-hero")

    def test_course_renders_optional_fallback_and_accessible_collapse(self):
        course = Formar.objects.create(
            title="Curso de prueba",
            plataforma="Plataforma de prueba",
            descripcion="<p>Descripción temporal</p>",
            fecha_finalizacion=date(2025, 1, 1),
        )

        response = self.client.get(reverse("formacion"))

        self.assertContains(response, course.title)
        self.assertContains(response, "Certificado no disponible")
        self.assertContains(response, 'type="button"')
        self.assertContains(response, f'aria-controls="curso-descripcion-{course.pk}"')
        self.assertNotContains(response, "placeholder.png")

    def test_academic_training_renders_without_certificate_or_end_date(self):
        training = FormacionAcademica.objects.create(
            institucion="Institución de prueba",
            titulo="Titulación de prueba",
            fecha_inicio=date(2024, 9, 1),
            en_curso=True,
        )

        response = self.client.get(reverse("experiencia"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, training.titulo)
        self.assertContains(response, "Actualmente")
        self.assertContains(response, "Certificado no disponible")
        self.assertNotContains(response, "placeholder.png")
