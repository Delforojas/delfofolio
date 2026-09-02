# Gestión de contenido

DelfoFolio utiliza el panel de Django Admin en `/admin/` para mantener el contenido administrable. Las apps registran sus modelos con configuraciones de administración específicas.

## Qué se gestiona desde Admin

- Proyectos generales y dashboards Power BI desde `portfolio/admin.py`.
- Categoría, tecnologías, imagen, demo y repositorio de GitHub de cada proyecto.
- Datasets con imagen, enlace de GitHub y archivo HTML.
- Cursos con descripción enriquecida mediante `RichTextField`, enlaces y certificados.
- Formación académica con fechas, notas y certificados.
- Experiencia laboral con empresa, ubicación, periodo, descripción y certificado.

Los administradores de portfolio incluyen filtros y búsquedas para los campos principales. En formación se muestran también previsualizaciones de certificados cuando existen.

## Multimedia

Los `ImageField` y `FileField` guardan rutas relativas bajo `media/`. La configuración utiliza:

- `MEDIA_URL = /media/`
- `MEDIA_ROOT = BASE_DIR / media`

La carpeta `media/` contiene contenido del portfolio y debe revisarse por separado antes de publicar archivos nuevos. No debe utilizarse como almacén automático de datos privados de producción.
