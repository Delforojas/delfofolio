# Portfolio y modelos de contenido

## Proyectos y dashboards

`portfolio.models.Project` concentra los proyectos del sitio. Cada registro tiene título, descripción, imagen, tecnologías, fecha y enlaces opcionales a una web y a GitHub.

El campo `category` distingue dos tipos:

- `general`: proyectos que aparecen en `/portfolio/`.
- `power_bi`: dashboards que aparecen en `/dashboards/`.

Las vistas aplican estos filtros antes de renderizar `portfolio/portfolio.html` o `portfolio/dashboards.html`. Ambas páginas reutilizan el parcial `_project_section.html`.

## Otros modelos

- `Dataset`: título, descripción, imagen, enlace de GitHub y archivo HTML.
- `Formar`: cursos, plataforma, instructor, duración, descripción enriquecida, enlace y certificado.
- `FormacionAcademica`: institución, titulación, disciplina, fechas, estado, nota y certificado.
- `ExperienciaLaboral`: cargo, tipo de empleo, empresa, ubicación, fechas, estado, descripción y certificado.

Estos modelos permiten que las páginas públicas consulten contenido persistente sin incluirlo directamente en los templates.

## Rutas relacionadas

- `/portfolio/`: proyectos generales.
- `/dashboards/`: proyectos categorizados como Power BI.
- `/dataset/`: datasets y recursos.
- `/formacion/`: cursos.
- `/experiencia/`: formación académica.
- `/experiencialaboral/`: experiencia profesional.

Los modelos utilizan ordenaciones por fecha para mostrar primero el contenido más reciente o, en formación académica, el periodo más reciente.
