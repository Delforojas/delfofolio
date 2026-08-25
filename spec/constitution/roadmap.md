# Roadmap del proyecto

## Estado actual del repositorio

El repositorio presenta un proyecto ya implementado, con varias secciones funcionales y modelos de contenido. Se puede documentar el estado actual sin inventar hitos futuros.

## Funcionalidades ya existentes

Se puede afirmar con evidencia que el proyecto ya incluye:

- portada o home
- página acerca de
- sección visual de tecnologías
- contacto
- portafolio con listados de proyectos
- sección independiente de dashboards Power BI
- sección de datasets/recursos
- formación: cursos
- formación académica
- experiencia laboral
- administración del contenido mediante Django Admin

Estas funcionalidades se observan en:

- `webpersonal/urls.py`
- `core/views.py`
- `portfolio/views.py`
- `formacion/views.py`
- `laboral/views.py`
- `dataset/views.py`
- modelos de cada app
- plantillas en los directorios `templates/`

## Funcionalidad Power BI

La siguiente funcionalidad está implementada y preparada para recibir contenido real:

- sección principal Dashboards para mostrar proyectos Power BI administrables mediante el modelo de proyectos existente

Dashboards dispone de navegación, ruta y página propias, mientras que Portfolio muestra exclusivamente proyectos generales. Su alcance, plan y tareas se documentan en `spec/features/008-power-bi/`. El usuario proporcionará posteriormente el contenido real; no se han creado registros ficticios.

## Observación sobre alcance

El proyecto actual parece estar centrado en la publicación estática de contenido profesional y administrable, no en una aplicación multi-tenant, API o sistema de autenticación complejo. Esa conclusión se desprende de la estructura actual y de la ausencia de evidencia de otras capas funcionales.

## Resumen de roadmap posible, basado en evidencia

El “roadmap” observable del repositorio es el siguiente:

1. Publicar contenido de perfil profesional.
2. Gestionar proyectos de portafolio.
3. Gestionar formación y certificados.
4. Gestionar experiencia laboral.
5. Publicar datasets o recursos.
6. Exponer todo a través de plantillas Django y rutas públicas.
7. Permitir edición mediante Django Admin.
8. Incorporar Dashboards como sección principal independiente reutilizando el modelo y la arquitectura de portfolio.
9. Modernizar el sistema visual y responsive de todas las vistas públicas sin cambiar la arquitectura ni los datos (implementada; revisión visual manual pendiente).
10. Incorporar Tecnologías como sección principal con un catálogo estático estructurado e iconos locales (implementada y validada).

No se incluyen otros hitos no observados ni supuestos de negocio.
