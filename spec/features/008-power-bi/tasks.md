# Tareas de la feature 008: Dashboards Power BI

## Estado

Separación implementada y validada técnicamente.

## Navegación y rutas

- [x] T001 Añadir la ruta `/dashboards/` con nombre `dashboards`.
- [x] T002 Añadir Dashboards al desplegable Proyectos después de Web Apps y antes de Datasets.
- [x] T003 Mantener Dashboards dentro de la app `portfolio` sin crear una app nueva.

## Vistas y filtrado

- [x] T004 Hacer que la vista Portfolio consulte solo proyectos generales.
- [x] T005 Crear la vista Dashboards para consultar solo proyectos Power BI.
- [x] T006 Mantener el orden descendente definido por `Project`.
- [x] T007 No modificar el modelo, Django Admin ni los datos.

## Plantillas

- [x] T008 Eliminar la subsección Power BI de `portfolio.html`.
- [x] T009 Crear `dashboards.html` como página independiente.
- [x] T010 Reutilizar `core/base.html`, el encabezado y los estilos existentes.
- [x] T011 Reutilizar `_project_section.html` para ambos listados.
- [x] T012 Mantener imagen, título, descripción, tecnologías y enlaces de Dashboard.
- [x] T013 Mantener el estado vacío en español y los enlaces externos seguros.
- [x] T014 No añadir datos ni contenido de proyectos ficticio.

## Pruebas

- [x] T015 Probar que Portfolio responde y solo muestra proyectos generales.
- [x] T016 Probar que Dashboards responde y solo muestra proyectos Power BI.
- [x] T017 Probar que las categorías no aparecen en la página incorrecta.
- [x] T018 Probar el orden de navegación Web Apps > Dashboards > Datasets dentro de Proyectos.
- [x] T019 Probar los datos y enlaces de un dashboard.
- [x] T020 Probar enlaces opcionales y estado vacío.
- [x] T021 Probar el orden descendente de Dashboards.

## Documentación

- [x] T022 Actualizar `spec.md` con la sección principal independiente.
- [x] T023 Actualizar `plan.md` con las dos rutas y vistas.
- [x] T024 Actualizar `tasks.md` con la corrección implementada.
- [x] T025 Actualizar misión y roadmap.

## Validación

- [x] T026 Ejecutar `python manage.py makemigrations --check --dry-run`.
- [x] T027 Ejecutar `python manage.py test portfolio`.
- [x] T028 Ejecutar `python manage.py test`.
- [x] T029 Ejecutar `python manage.py check`.
- [x] T030 Comprobar `/portfolio/` y `/dashboards/` con el cliente Django.
- [x] T031 Confirmar que no se modificaron modelos, Admin, migraciones, dependencias ni datos.

## Criterio de finalización

La corrección está terminada: ambas rutas funcionan, cada una muestra exclusivamente su categoría, la navegación las agrupa bajo Proyectos en el orden solicitado y todas las validaciones automáticas finalizan sin errores propios de la feature.
