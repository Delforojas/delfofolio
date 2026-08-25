from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import ExperienciaLaboral


class ExperienciaLaboralPageTests(TestCase):
    def test_empty_page_has_spanish_empty_state(self):
        response = self.client.get(reverse("experiencialaboral"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Aún no se han registrado experiencias laborales.",
        )

    def test_experience_renders_responsive_card_and_accessible_details(self):
        experience = ExperienciaLaboral.objects.create(
            cargo="Cargo de prueba",
            tipo_empleo="Jornada completa",
            empresa="Empresa de prueba",
            fecha_inicio=date(2020, 1, 1),
            actualmente=True,
            descripcion="Descripción temporal de prueba",
        )

        response = self.client.get(reverse("experiencialaboral"))

        self.assertContains(response, experience.cargo)
        self.assertContains(response, "Imagen no disponible")
        self.assertContains(response, 'type="button"')
        self.assertContains(response, f'aria-controls="puesto-descripcion-{experience.pk}"')
        self.assertNotContains(response, "placeholder.png")
