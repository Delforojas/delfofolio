# Plan de la feature 008: Dashboards Power BI

## Estado

Plan aprobado, implementado y validado técnicamente.

## Contexto

La primera implementación presentó Power BI como una subsección dentro de `/portfolio/`. El requisito corregido mantiene para Dashboards una ruta y página propias, accesibles desde el desplegable principal Proyectos.

La separación es exclusivamente de presentación y navegación. El dominio sigue siendo `portfolio` porque ambos tipos de contenido comparten `Project` y Django Admin.

## Decisiones de implementación

### Modelo y administración

No se modifica `Project`. Sus campos actuales ya cubren categoría, tecnologías, enlace principal y GitHub.

No se modifica `ProjectAdmin`. Los dashboards continúan administrándose desde Portfolio > Proyectos seleccionando `Tipo = Power BI`.

No se necesita migración ni modificación de datos.

### Rutas y vistas

Se mantienen dos vistas dentro de `portfolio/views.py`:

- `portfolio`: filtra `Project.Category.GENERAL`.
- `dashboards`: filtra `Project.Category.POWER_BI`.

`webpersonal/urls.py` publica:

- `/portfolio/`, nombre `portfolio`.
- `/dashboards/`, nombre `dashboards`.

### Navegación

`core/templates/core/base.html` agrupa Web Apps, Dashboards y Datasets dentro del desplegable Proyectos, reutilizando el patrón de Formación.

### Plantillas

`portfolio/templates/portfolio/portfolio.html` conserva únicamente el listado general.

`portfolio/templates/portfolio/dashboards.html` es una página independiente que:

- hereda de `core/base.html`;
- usa el encabezado visual existente;
- carga `fondo2.css`;
- reutiliza `portfolio/_project_section.html`;
- muestra exclusivamente el queryset Power BI;
- conserva el estado vacío y los enlaces seguros.

El parcial `_project_section.html` no necesita cambios.

### Estilos

No se añaden estilos. La nueva página reutiliza las clases responsive ya implementadas en `custom2.css`, la cuadrícula Bootstrap y `fondo2.css`.

## Archivos modificados

- `webpersonal/urls.py`
- `core/templates/core/base.html`
- `portfolio/views.py`
- `portfolio/templates/portfolio/portfolio.html`
- `portfolio/tests.py`
- `spec/features/008-power-bi/spec.md`
- `spec/features/008-power-bi/plan.md`
- `spec/features/008-power-bi/tasks.md`
- `spec/constitution/mission.md`
- `spec/constitution/roadmap.md`

## Archivo creado

- `portfolio/templates/portfolio/dashboards.html`

## Archivos sin cambios

- `portfolio/models.py`
- `portfolio/admin.py`
- `portfolio/migrations/`
- `db.sqlite3`
- `requirements.txt`
- `core/static/`
- `staticfiles/`

## Estrategia de pruebas

- comprobar respuesta 200 y plantilla de `/portfolio/`;
- comprobar que Portfolio solo recibe y muestra proyectos generales;
- comprobar respuesta 200 y plantilla de `/dashboards/`;
- comprobar que Dashboards solo recibe y muestra proyectos Power BI;
- comprobar que cada página excluye el contenido de la otra;
- comprobar el orden Web Apps > Dashboards > Datasets dentro de Proyectos;
- comprobar datos, enlaces seguros, campos opcionales y estado vacío;
- comprobar el orden descendente de Dashboards.

## Verificación

```bash
python manage.py makemigrations --check --dry-run
python manage.py test portfolio
python manage.py test
python manage.py check
```

También se comprobarán `/portfolio/` y `/dashboards/` mediante el cliente de pruebas de Django. No se crearán datos persistentes para la verificación.

## Resultado esperado

Dos páginas independientes que reutilizan el mismo modelo y componente visual: Web Apps para proyectos generales y Dashboards para proyectos Power BI, agrupadas junto a Datasets bajo Proyectos.
