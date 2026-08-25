# Feature 008: Dashboards Power BI

## Estado

Implementada y validada técnicamente. Pendiente únicamente de comprobación visual manual en navegadores reales.

## Descripción

Incorporar "Dashboards" como una sección independiente de la web personal. La sección dispone de su propia ruta y página, muestra exclusivamente los registros de `Project` clasificados como Power BI y se accede desde el desplegable principal "Proyectos".

Portfolio y Dashboards comparten el modelo, la administración, el componente visual y los estilos, pero no comparten contenido público:

- Portfolio muestra únicamente proyectos generales.
- Dashboards muestra únicamente proyectos Power BI.

## Objetivo

Permitir que los visitantes accedan directamente a los dashboards desde `Proyectos > Dashboards`, sin crear un modelo ni una app adicionales.

## Datos de un dashboard

Cada registro puede mostrar:

- imagen o captura
- título
- descripción
- tecnologías utilizadas
- enlace al dashboard interactivo de Power BI
- enlace al repositorio de GitHub

Los datos concretos serán proporcionados por el usuario. La feature no crea registros, textos de proyectos, imágenes, tecnologías ni URLs ficticias.

## Historias de usuario

### US1. Acceder a Dashboards desde Proyectos

Como visitante, quiero encontrar "Dashboards" dentro del desplegable "Proyectos", después de "Web Apps" y antes de "Datasets", para acceder directamente a esa sección.

### US2. Consultar exclusivamente dashboards

Como visitante, quiero que `/dashboards/` muestre solo proyectos Power BI para no mezclarlos con el portfolio general.

### US3. Consultar exclusivamente proyectos generales

Como visitante, quiero que `/portfolio/` muestre solo proyectos generales y no contenga una subsección Power BI.

### US4. Administrar todo desde un único modelo

Como administrador, quiero seguir creando dashboards desde Portfolio > Proyectos en Django Admin, seleccionando `Tipo = Power BI`.

## Requisitos funcionales

- RF-01: Debe existir una ruta pública `/dashboards/` con nombre `dashboards`.
- RF-02: La navegación principal debe agrupar "Web Apps", "Dashboards" y "Datasets", en ese orden, dentro del desplegable "Proyectos".
- RF-03: `/dashboards/` debe disponer de una vista y una plantilla propias.
- RF-04: `/dashboards/` debe mostrar exclusivamente `Project` con categoría `POWER_BI`.
- RF-05: `/portfolio/` debe mostrar exclusivamente `Project` con categoría `GENERAL`.
- RF-06: Portfolio no debe contener un encabezado, listado ni estado vacío de Power BI.
- RF-07: Los dashboards deben continuar perteneciendo al modelo `Project`.
- RF-08: La gestión debe continuar en Portfolio > Proyectos de Django Admin.
- RF-09: La página Dashboards debe mostrar imagen, título, descripción y tecnologías cuando estén disponibles.
- RF-10: El enlace principal de un proyecto Power BI debe abrir el dashboard interactivo.
- RF-11: El enlace de GitHub debe mostrarse de forma independiente cuando exista.
- RF-12: Los enlaces externos solo deben renderizarse cuando tengan valor.
- RF-13: Los enlaces externos deben usar `target="_blank"` y `rel="noopener noreferrer"`.
- RF-14: Sin proyectos Power BI, Dashboards debe mostrar un estado vacío en español.
- RF-15: Ambas páginas deben mantener el orden descendente por fecha de creación.

## Requisitos no funcionales

- RNF-01: Mantener Django, plantillas, Bootstrap y los assets actuales.
- RNF-02: No añadir dependencias, modelos, apps ni migraciones.
- RNF-03: Reutilizar `portfolio/_project_section.html` para el listado de ambas páginas.
- RNF-04: Reutilizar `fondo2.css`, `custom2.css` y el encabezado visual existente.
- RNF-05: Mantener el comportamiento responsive en móvil, tablet y escritorio.
- RNF-06: Mantener todos los textos visibles en español.
- RNF-07: No editar `staticfiles/` ni modificar datos existentes.

## Criterios de aceptación

- CA-01: `/portfolio/` responde correctamente y solo contiene proyectos generales.
- CA-02: `/dashboards/` responde correctamente y solo contiene proyectos Power BI.
- CA-03: Un proyecto Power BI no aparece en Portfolio.
- CA-04: Un proyecto general no aparece en Dashboards.
- CA-05: Portfolio no contiene una subsección Power BI.
- CA-06: El desplegable Proyectos contiene Web Apps, Dashboards y Datasets en ese orden y conserva sus URLs actuales.
- CA-07: Dashboards usa el layout global y el componente compartido de proyectos.
- CA-08: Un dashboard puede mostrar captura, título, descripción, tecnologías y ambos enlaces.
- CA-09: Los enlaces opcionales ausentes no producen enlaces vacíos ni errores.
- CA-10: Sin dashboards se muestra un mensaje vacío en español.
- CA-11: El modelo y Django Admin no cambian.
- CA-12: No se genera ni aplica ninguna migración para esta corrección.
- CA-13: Las pruebas verifican la separación de rutas y categorías.
- CA-14: `python manage.py check` y `python manage.py test` finalizan sin errores propios de la feature.

## Fuera de alcance

- Crear un modelo `Dashboard` o `PowerBIProject`.
- Crear una app Django adicional.
- Cambiar los campos de `Project` o Django Admin.
- Crear o modificar migraciones.
- Añadir dashboards o contenido real.
- Incrustar informes mediante iframe o añadir Power BI JavaScript SDK.
- Cambiar el diseño global del sitio.

## Evidencia de implementación

- `webpersonal/urls.py` publica `/portfolio/` y `/dashboards/`.
- `core/templates/core/base.html` contiene el enlace a Dashboards dentro del desplegable Proyectos.
- `portfolio/views.py` filtra cada categoría en una vista independiente.
- `portfolio/templates/portfolio/portfolio.html` renderiza proyectos generales.
- `portfolio/templates/portfolio/dashboards.html` renderiza proyectos Power BI.
- `portfolio/templates/portfolio/_project_section.html` es el componente visual compartido.
- `portfolio/models.py` y `portfolio/admin.py` mantienen el modelo y la administración únicos.
