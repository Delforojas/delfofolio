# Tareas de la feature 010: Tecnologías

## Estado

Feature implementada y validada técnica y visualmente.

## Catálogo e iconos

- [x] T001 Aprobar las cuatro categorías y las 24 tecnologías.
- [x] T002 Comprobar la disponibilidad de los símbolos en Simple Icons.
- [x] T003 Aprobar las fuentes alternativas y la equivalencia para DAX.
- [x] T004 Crear el sprite SVG local con los 24 símbolos.
- [x] T005 Documentar fuentes, licencias y equivalencias de iconos.

## Vista y navegación

- [x] T006 Definir el catálogo ordenado en `core/views.py`.
- [x] T007 Crear la vista `tecnologias`.
- [x] T008 Publicar `/tecnologias/` con nombre `tecnologias`.
- [x] T009 Añadir Tecnologías después de Acerca de en el menú.
- [x] T010 Implementar el estado activo accesible.

## Template y estilos

- [x] T011 Crear `core/tecnologias.html`.
- [x] T012 Reutilizar el layout, cabecera y fondo globales.
- [x] T013 Renderizar categorías y tarjetas mediante bucles.
- [x] T014 Implementar el grid responsive mobile-first.
- [x] T015 Añadir un hover sutil y respetar movimiento reducido.
- [x] T016 Verificar iconos decorativos, nombres visibles y estructura semántica.

## Pruebas y documentación

- [x] T017 Probar ruta, template, contexto y estado activo.
- [x] T018 Probar categorías, orden y total de tecnologías.
- [x] T019 Probar el orden de navegación.
- [x] T020 Probar que todos los símbolos referenciados existen localmente.
- [x] T021 Probar ausencia de cargas externas de iconos.
- [x] T022 Añadir la feature al índice SDD.
- [x] T023 Actualizar misión y roadmap.

## Validación

- [x] T024 Ejecutar `python manage.py makemigrations --check --dry-run`.
- [x] T025 Ejecutar `python manage.py check`.
- [x] T026 Ejecutar `python manage.py test`.
- [x] T027 Comprobar `/tecnologias/` con el cliente Django.
- [x] T028 Revisar móvil, tablet y escritorio.
- [x] T029 Comprobar visualmente los iconos del catálogo inicial.
- [x] T030 Confirmar que no se modificaron modelos, Admin, dependencias ni datos.
- [x] T031 Aplicar colores de marca sin fondos propios y con contraste sobre las tarjetas.

## Validación visual

La inspección del catálogo inicial se completó con SafariDriver en viewports de 390 px, 768 px y 1440 px. Los grids muestran respectivamente 2, 4 y 6 columnas, no existe overflow horizontal y sus 18 iconos son visibles.

## Ampliación del catálogo

- [x] T032 Diagnosticar las referencias sin símbolo de Angular, PHP, TypeScript y Symfony.
- [x] T033 Añadir los símbolos oficiales de Angular, PHP, TypeScript y Symfony al sprite.
- [x] T034 Añadir Anaconda y Scikit-learn a Datos y Business Intelligence.
- [x] T035 Añadir los símbolos oficiales de Anaconda y scikit-learn al sprite.
- [x] T036 Adaptar el contraste de Angular y Symfony sin modificar sus paths.
- [x] T037 Validar las 24 referencias, los seis iconos ampliados y la ruta pública.

La ampliación se validó con la suite completa de Django y SafariDriver. Los seis iconos tienen referencias locales, geometría visible de 56 x 56 px y sus colores o adaptaciones de contraste esperadas.
