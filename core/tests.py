from pathlib import Path
from xml.etree import ElementTree

from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from django.utils.html import escape

from .views import TECHNOLOGY_CATEGORIES


class PublicPageTests(TestCase):
    def test_static_pages_render_with_shared_accessible_layout(self):
        for url_name in ("home", "about", "tecnologias", "contact"):
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, 'href="#contenido-principal"')
                self.assertContains(response, 'id="contenido-principal"')
                self.assertContains(response, 'aria-label="Navegación principal"')
                self.assertContains(response, 'aria-current="page"')
                self.assertContains(response, "core/css/site.css")
                self.assertContains(response, 'id="hexCanvas"', count=1)
                self.assertContains(response, "p5.min.js", count=1)
                self.assertContains(response, "core/vendor/jquery/fondo.js", count=1)
                self.assertNotContains(response, "core/vendor/jquery/fondo3.js")

    def test_technologies_page_renders_approved_catalog(self):
        response = self.client.get(reverse("tecnologias"))
        technology_count = sum(
            len(category["technologies"])
            for category in TECHNOLOGY_CATEGORIES
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/tecnologias.html")
        self.assertEqual(response.context["technology_categories"], TECHNOLOGY_CATEGORIES)
        self.assertContains(
            response,
            'class="technology-category"',
            count=len(TECHNOLOGY_CATEGORIES),
        )
        self.assertEqual(technology_count, 31)
        self.assertContains(response, 'class="technology-card"', count=technology_count)

        for category in TECHNOLOGY_CATEGORIES:
            self.assertContains(response, escape(category["name"]))
            for technology in category["technologies"]:
                self.assertContains(response, technology["name"])

    def test_projects_dropdown_has_expected_order_and_destinations(self):
        response = self.client.get(reverse("tecnologias"))
        content = response.content.decode()

        about_position = content.index(f'href="{reverse("about")}"')
        technologies_position = content.index(f'href="{reverse("tecnologias")}"')
        projects_position = content.index('id="projectsDropdown"')
        portfolio_position = content.index(f'href="{reverse("portfolio")}"')
        dashboards_position = content.index(f'href="{reverse("dashboards")}"')
        dataset_position = content.index(f'href="{reverse("dataset")}"')
        training_position = content.index('id="formacionDropdown"')
        work_position = content.index(f'href="{reverse("experiencialaboral")}"')
        contact_position = content.index(f'href="{reverse("contact")}"')

        self.assertLess(about_position, technologies_position)
        self.assertLess(technologies_position, projects_position)
        self.assertLess(projects_position, portfolio_position)
        self.assertLess(portfolio_position, dashboards_position)
        self.assertLess(dashboards_position, dataset_position)
        self.assertLess(dataset_position, training_position)
        self.assertLess(training_position, work_position)
        self.assertLess(work_position, contact_position)
        self.assertContains(response, 'aria-labelledby="projectsDropdown"')
        self.assertContains(response, "Proyectos")
        self.assertContains(response, ">Web Apps</a>")

    def test_projects_dropdown_marks_parent_and_current_page(self):
        for url_name in ("portfolio", "dashboards", "dataset"):
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))

                self.assertContains(
                    response,
                    'class="nav-link dropdown-toggle active"\n'
                    '              href="#"\n'
                    '              id="projectsDropdown"',
                )
                self.assertContains(
                    response,
                    f'href="{reverse(url_name)}" aria-current="page"',
                )

    def test_technologies_navigation_follows_about(self):
        response = self.client.get(reverse("tecnologias"))
        content = response.content.decode()

        about_position = content.index(f'href="{reverse("about")}"')
        technologies_position = content.index(f'href="{reverse("tecnologias")}"')
        projects_position = content.index('id="projectsDropdown"')

        self.assertLess(about_position, technologies_position)
        self.assertLess(technologies_position, projects_position)
        self.assertContains(response, 'href="/tecnologias/" aria-current="page"')

    def test_technology_icons_are_local_and_present_in_sprite(self):
        response = self.client.get(reverse("tecnologias"))
        sprite = Path(
            settings.BASE_DIR,
            "core/static/core/img/technology-icons.svg",
        ).read_text(encoding="utf-8")

        referenced_icons = {
            technology["icon"]
            for category in TECHNOLOGY_CATEGORIES
            for technology in category["technologies"]
        }
        symbols = {
            element.attrib["id"]: element
            for element in ElementTree.fromstring(sprite)
            if element.tag.endswith("symbol")
        }

        self.assertEqual(len(referenced_icons), 31)
        self.assertContains(
            response,
            "core/img/technology-icons.svg#",
            count=len(referenced_icons),
        )
        self.assertContains(response, "--technology-color:", count=len(referenced_icons))
        self.assertNotContains(response, "cdn.simpleicons.org")
        for icon in referenced_icons:
            self.assertIn(icon, symbols)
            self.assertIsNotNone(symbols[icon].attrib.get("viewBox"))
            self.assertTrue(
                any(element.tag.endswith("path") for element in symbols[icon].iter())
            )

    def test_requested_technology_icon_references_match_the_sprite(self):
        response = self.client.get(reverse("tecnologias"))
        required_technologies = {
            "Angular": "angular",
            "PHP": "php",
            "TypeScript": "typescript",
            "Symfony": "symfony",
            "Anaconda": "anaconda",
            "Scikit-learn": "scikitlearn",
        }
        catalog = {
            technology["name"]: technology["icon"]
            for category in TECHNOLOGY_CATEGORIES
            for technology in category["technologies"]
        }
        sprite_path = Path(settings.BASE_DIR) / "core/static/core/img/technology-icons.svg"
        symbols = {
            element.attrib["id"]: element
            for element in ElementTree.parse(sprite_path).getroot()
            if element.tag.endswith("symbol")
        }

        for name, icon in required_technologies.items():
            self.assertEqual(catalog.get(name), icon)
            self.assertContains(response, f"technology-icons.svg#{icon}")
            self.assertEqual(symbols[icon].attrib.get("viewBox"), "0 0 24 24")
            self.assertTrue(
                any(element.tag.endswith("path") for element in symbols[icon].iter())
            )

    def test_new_technology_icon_references_match_the_sprite(self):
        response = self.client.get(reverse("tecnologias"))
        required_technologies = {
            "OpenCode": "opencode",
            "OpenAI": "openai",
            "MCP": "modelcontextprotocol",
            "Agent Skills": "agentskills",
            "phpMyAdmin": "phpmyadmin",
            "PostgreSQL": "postgresql",
            "MySQL": "mysql",
        }
        catalog = {
            technology["name"]: technology["icon"]
            for category in TECHNOLOGY_CATEGORIES
            for technology in category["technologies"]
        }
        sprite_path = Path(settings.BASE_DIR) / "core/static/core/img/technology-icons.svg"
        symbols = {
            element.attrib["id"]: element
            for element in ElementTree.parse(sprite_path).getroot()
            if element.tag.endswith("symbol")
        }

        for name, icon in required_technologies.items():
            self.assertEqual(catalog.get(name), icon)
            self.assertContains(response, f"technology-icons.svg#{icon}")
            self.assertIn(icon, symbols)
            self.assertIsNotNone(symbols[icon].attrib.get("viewBox"))
            self.assertTrue(
                any(element.tag.endswith("path") for element in symbols[icon].iter())
            )

    def test_legacy_custom_styles_and_hover_scripts_are_not_loaded(self):
        response = self.client.get(reverse("home"))

        self.assertNotContains(response, "core/css/clean-blog.min.css")
        self.assertNotContains(response, "core/css/custom.css")
        self.assertNotContains(response, "core/css/custom2.css")
        self.assertNotContains(response, "core/css/fondo2.css")
        self.assertNotContains(response, "hover_proyectos.js")
        self.assertNotContains(response, "vendor/jquery/custom.js")

    def test_contact_uses_existing_accessible_contact_links(self):
        response = self.client.get(reverse("contact"))

        self.assertContains(response, "mailto:delfinrojasespina@gmail.com", count=2)
        self.assertContains(response, "https://github.com/Delforojas", count=2)
        self.assertContains(response, "https://www.linkedin.com/in/delfinrojas", count=2)
        self.assertContains(response, "itsjust Delfo")
        self.assertContains(response, "itsjust_Delfo")

    def test_contact_uses_local_instagram_and_facebook_icons(self):
        response = self.client.get(reverse("contact"))
        sprite_path = Path(settings.BASE_DIR) / "core/static/core/img/technology-icons.svg"
        symbols = {
            element.attrib["id"]: element
            for element in ElementTree.parse(sprite_path).getroot()
            if element.tag.endswith("symbol")
        }

        self.assertContains(response, "technology-icons.svg#instagram")
        self.assertContains(response, "technology-icons.svg#facebook")
        self.assertContains(response, "color: #FF0069")
        self.assertContains(response, "color: #0866FF")
        for icon in ("instagram", "facebook"):
            self.assertIn(icon, symbols)
            self.assertEqual(symbols[icon].attrib.get("viewBox"), "0 0 24 24")
            self.assertTrue(
                any(element.tag.endswith("path") for element in symbols[icon].iter())
            )
