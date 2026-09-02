from django.test import TestCase
from django.urls import reverse

from .models import Project


def create_project(title, category=Project.Category.GENERAL, **kwargs):
    defaults = {
        "description": f"Descripción de prueba para {title}",
        "image": "projects/test.png",
        "category": category,
    }
    defaults.update(kwargs)
    return Project.objects.create(title=title, **defaults)


class ProjectModelTests(TestCase):
    def test_new_projects_are_general_by_default(self):
        project = create_project("Proyecto general")

        self.assertEqual(project.category, Project.Category.GENERAL)

    def test_project_supports_power_bi_fields_and_long_urls(self):
        project = create_project(
            "Panel de prueba",
            category=Project.Category.POWER_BI,
            technologies="Power BI, DAX",
            link="https://powerbi.example/informe",
            github_link="https://github.example/repositorio",
        )

        self.assertEqual(project.technologies, "Power BI, DAX")
        self.assertEqual(Project._meta.get_field("link").max_length, 500)
        self.assertEqual(Project._meta.get_field("github_link").max_length, 500)


class PortfolioAndDashboardsViewTests(TestCase):
    def setUp(self):
        self.general_project = create_project("Proyecto general")
        self.power_bi_project = create_project(
            "Panel de prueba",
            category=Project.Category.POWER_BI,
            technologies="Power BI, DAX",
            link="https://powerbi.example/informe",
            github_link="https://github.example/repositorio",
        )
        self.portfolio_url = reverse("portfolio")
        self.dashboards_url = reverse("dashboards")

    def test_portfolio_only_displays_general_projects(self):
        response = self.client.get(self.portfolio_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/portfolio.html")
        self.assertQuerySetEqual(response.context["projects"], [self.general_project])
        self.assertContains(response, self.general_project.title)
        self.assertNotContains(response, self.power_bi_project.title)
        self.assertNotContains(response, 'id="power-bi-title"')

    def test_dashboards_only_displays_power_bi_projects(self):
        response = self.client.get(self.dashboards_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/dashboards.html")
        self.assertQuerySetEqual(response.context["projects"], [self.power_bi_project])
        self.assertContains(response, self.power_bi_project.title)
        self.assertNotContains(response, self.general_project.title)

    def test_projects_dropdown_orders_web_apps_dashboards_and_datasets(self):
        response = self.client.get(self.dashboards_url)
        content = response.content.decode()

        projects_position = content.index('id="projectsDropdown"')
        portfolio_position = content.index(f'href="{self.portfolio_url}"')
        dashboards_position = content.index(f'href="{self.dashboards_url}"')
        dataset_position = content.index(f'href="{reverse("dataset")}"')

        self.assertLess(projects_position, portfolio_position)
        self.assertLess(portfolio_position, dashboards_position)
        self.assertLess(dashboards_position, dataset_position)
        self.assertContains(response, ">Web Apps</a>")
        self.assertContains(response, ">Dashboards</a>")
        self.assertContains(response, ">Datasets</a>")

    def test_dashboards_renders_project_data_and_secure_links(self):
        response = self.client.get(self.dashboards_url)

        self.assertContains(response, 'id="power-bi-title"')
        self.assertContains(response, "Power BI")
        self.assertContains(response, self.power_bi_project.title)
        self.assertContains(response, self.power_bi_project.technologies)
        self.assertContains(response, f'href="{self.power_bi_project.link}"')
        self.assertContains(response, f'href="{self.power_bi_project.github_link}"')
        self.assertContains(response, 'target="_blank"', count=4)
        self.assertContains(response, 'rel="noopener noreferrer"', count=4)
        self.assertContains(response, "Ver dashboard interactivo")
        self.assertContains(response, "Ver repositorio en GitHub")

    def test_project_images_use_lazy_loading_and_contextual_alt_text(self):
        response = self.client.get(self.dashboards_url)

        self.assertContains(response, 'loading="lazy"')
        self.assertContains(response, f'alt="Captura de {self.power_bi_project.title}"')

    def test_optional_links_are_not_rendered_when_empty(self):
        self.power_bi_project.link = None
        self.power_bi_project.github_link = None
        self.power_bi_project.save()

        response = self.client.get(self.dashboards_url)

        self.assertNotContains(response, "Ver dashboard interactivo")
        self.assertNotContains(response, "Ver repositorio en GitHub")

    def test_dashboards_displays_spanish_empty_state(self):
        self.power_bi_project.delete()

        response = self.client.get(self.dashboards_url)

        self.assertContains(
            response,
            "No hay dashboards de Power BI publicados todavía.",
        )

    def test_dashboards_keeps_descending_creation_order(self):
        newer_project = create_project(
            "Panel más reciente",
            category=Project.Category.POWER_BI,
        )

        response = self.client.get(self.dashboards_url)

        self.assertQuerySetEqual(
            response.context["projects"],
            [newer_project, self.power_bi_project],
        )
