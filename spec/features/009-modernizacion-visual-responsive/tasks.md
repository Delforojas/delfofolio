# Tareas de la feature 009: Modernización visual y responsive

## Documentación

- [x] T001 Crear la feature SDD 009.
- [x] T002 Documentar requisitos visuales, responsive, accesibilidad y rendimiento.
- [x] T003 Actualizar el estado final, README y roadmap.

## Sistema global

- [x] T004 Actualizar Bootstrap local a 4.6.2.
- [x] T005 Crear `site.css` y sustituir las capas CSS heredadas en la carga.
- [x] T006 Modernizar navegación, dropdown y estado activo.
- [x] T007 Añadir skip link, landmark `main` y foco visible.
- [x] T008 Modernizar footer y enlaces sociales accesibles.
- [x] T009 Crear el componente de cabecera interior.

## Secciones

- [x] T010 Migrar Portada.
- [x] T011 Migrar Acerca de.
- [x] T012 Migrar Contacto.
- [x] T013 Migrar Datasets y proteger archivos opcionales.
- [x] T014 Migrar Cursos.
- [x] T015 Migrar Formación académica.
- [x] T016 Migrar Experiencia laboral.
- [x] T017 Modernizar el parcial compartido de Portfolio y Dashboards.

## Rendimiento y accesibilidad

- [x] T018 Eliminar hover JavaScript de la carga y reemplazarlo por CSS.
- [x] T019 Añadir lazy loading y alt contextual a imágenes.
- [x] T020 Optimizar fondo completo y fondo interior.
- [x] T021 Respetar `prefers-reduced-motion`.
- [x] T022 Verificar áreas táctiles, foco y contraste.

## Pruebas y validación

- [x] T023 Añadir pruebas de las páginas estáticas y navegación.
- [x] T024 Añadir pruebas de listados y campos opcionales.
- [x] T025 Mantener y ampliar pruebas de Portfolio/Dashboards.
- [x] T026 Ejecutar `makemigrations --check --dry-run`.
- [x] T027 Ejecutar `python manage.py check`.
- [x] T028 Ejecutar tests específicos y suite completa.
- [x] T029 Comprobar todas las rutas públicas.
- [ ] T030 Revisar desktop, tablet, móvil y pantallas grandes.
- [ ] T031 Revisar overflow horizontal, teclado y foco.

## Validación manual pendiente

T030 y T031 requieren un navegador real. La estructura mobile-first, los breakpoints, el foco y las protecciones de overflow se han revisado en código, pero el entorno no dispone de automatización de navegador sin instalar dependencias adicionales.

## Ajuste de espaciado vertical

- [x] T032 Reducir globalmente la altura y padding móvil de las cabeceras interiores.
- [x] T033 Compactar secciones, tarjetas, imágenes, metadatos y acciones compartidas.
- [x] T034 Mantener una composición más amplia desde tablet mediante un único breakpoint.
- [x] T035 Validar tests, rutas y ausencia de cambios de modelo tras el ajuste.

## Fondo global

- [x] T036 Centralizar el canvas hexagonal en el layout compartido.
- [x] T037 Retirar canvas y cargas p5 duplicadas de las vistas.
- [x] T038 Ajustar cabeceras y footer para mostrar el patrón de forma continua.
- [x] T039 Validar checks y tests tras centralizar el fondo.
