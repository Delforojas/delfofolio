from django.test import TestCase
from django.urls import reverse

from .models import Dataset


class DatasetPageTests(TestCase):
    def test_empty_page_has_spanish_empty_state(self):
        response = self.client.get(reverse("dataset"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No se han registrado datasets todavía.")

    def test_dataset_without_optional_media_or_links_renders_safely(self):
        dataset = Dataset.objects.create(
            titulo="Dataset de prueba",
            descripcion="Descripción temporal de prueba",
        )

        response = self.client.get(reverse("dataset"))

        self.assertContains(response, dataset.titulo)
        self.assertContains(response, "Vista previa no disponible")
        self.assertNotContains(response, "Ver dataset")
        self.assertNotContains(response, "placeholder.png")

    def test_dataset_actions_render_as_secure_links(self):
        dataset = Dataset.objects.create(
            titulo="Dataset con enlaces",
            descripcion="Descripción temporal de prueba",
            github_url="https://github.example/dataset",
            archivo_html="certificados/dataset.html",
        )

        response = self.client.get(reverse("dataset"))

        self.assertContains(response, f'href="{dataset.github_url}"')
        self.assertContains(response, 'href="/media/certificados/dataset.html"')
        self.assertContains(response, 'rel="noopener noreferrer"', count=4)
        self.assertNotContains(response, "onclick=")
