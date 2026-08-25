# Feature 009: Modernización visual y responsive

## Estado

Implementada y validada técnicamente. Pendiente de revisión visual manual en navegadores reales.

## Objetivo

Modernizar todas las vistas públicas del portfolio manteniendo su identidad tecnológica, arquitectura Django, contenido real y navegación actual. La interfaz debe ser profesional, limpia, coherente, accesible y mobile-first.

## Alcance

- Portada
- Acerca de
- Datasets
- Cursos
- Formación académica
- Experiencia laboral
- Portfolio
- Dashboards
- Contacto
- Navegación y footer globales

## Requisitos funcionales

- RF-01: Todas las rutas y contenidos actuales deben conservarse.
- RF-02: Portfolio debe seguir mostrando proyectos generales y Dashboards proyectos Power BI.
- RF-03: Las cabeceras interiores deben reutilizar un componente común.
- RF-04: Los listados deben mostrar estados vacíos en español.
- RF-05: Las acciones externas deben ser enlaces descriptivos y seguros.
- RF-06: Los campos opcionales no deben producir errores de plantilla.
- RF-07: Contacto debe reutilizar únicamente las vías y URLs ya existentes.

## Requisitos visuales

- RV-01: Conservar turquesa, naranja, tipografía tecnológica y fondo hexagonal como identidad.
- RV-02: Usar una jerarquía tipográfica y una escala de espaciado consistentes.
- RV-03: Presentar contenidos en superficies legibles con contraste suficiente.
- RV-04: Unificar tarjetas, imágenes, metadatos, botones y estados interactivos.
- RV-05: Evitar efectos excesivos, fondos recargados y animaciones innecesarias.
- RV-06: Limitar la anchura de lectura y mantener composiciones equilibradas en pantallas grandes.
- RV-07: Evitar espacio vertical innecesario entre la navegación, las cabeceras y el contenido, especialmente en móvil.
- RV-08: Mantener tarjetas compactas sin reducir legibilidad ni áreas táctiles.
- RV-09: El fondo hexagonal debe ser único, global y continuo durante todo el scroll, sin cortes entre cabeceras y contenido.

## Responsive

- RSP-01: Implementación mobile-first.
- RSP-02: Navegación funcional sin desbordamiento entre 320 px y pantallas grandes.
- RSP-03: Tarjetas apiladas en móvil y distribuidas en columnas cuando exista espacio.
- RSP-04: Imágenes fluidas con proporción consistente.
- RSP-05: Botones y enlaces adaptables, con áreas táctiles mínimas de 44 px.
- RSP-06: No debe existir overflow horizontal en las rutas públicas.
- RSP-07: Tipografía y cabeceras deben usar tamaños fluidos.

## Accesibilidad

- A11Y-01: Añadir enlace para saltar al contenido y landmark `main`.
- A11Y-02: Navegación y dropdown deben exponer atributos ARIA correctos.
- A11Y-03: La página activa debe usar `aria-current="page"`.
- A11Y-04: Todos los controles deben mostrar un foco visible.
- A11Y-05: Iconos decorativos deben ocultarse a tecnologías asistivas.
- A11Y-06: Imágenes informativas deben tener textos alternativos contextuales.
- A11Y-07: La interfaz debe respetar `prefers-reduced-motion`.
- A11Y-08: La estructura de encabezados y elementos semánticos debe ser válida.

## Rendimiento

- PERF-01: No añadir dependencias visuales nuevas.
- PERF-02: Actualizar Bootstrap solo dentro de la versión 4.x aprobada.
- PERF-03: Sustituir hover JavaScript por CSS.
- PERF-04: Cargar imágenes de listados con `loading="lazy"` y `decoding="async"`.
- PERF-05: Reducir la frecuencia del fondo hexagonal y adaptarlo a resize, visibilidad y movimiento reducido.
- PERF-06: No editar `staticfiles/` manualmente.
- PERF-07: Cargar una única instancia de p5 y del generador hexagonal desde el layout compartido.

## Criterios de aceptación

- CA-01: Todas las rutas públicas responden sin errores de plantilla.
- CA-02: La navegación funciona con ratón, teclado y móvil.
- CA-03: Todas las páginas comparten navegación, cabecera, tipografía, tarjetas y footer coherentes.
- CA-04: Los listados mantienen los datos y condiciones actuales.
- CA-05: Portfolio y Dashboards conservan su separación.
- CA-06: Datasets no intenta resolver un archivo opcional ausente.
- CA-07: No existen referencias a placeholders inexistentes.
- CA-08: No se detecta overflow horizontal en los viewports de validación.
- CA-09: El foco es visible y el movimiento reducido desactiva transiciones no esenciales.
- CA-10: `python manage.py check` y `python manage.py test` finalizan sin errores propios de la feature.
- CA-11: `makemigrations --check --dry-run` no detecta cambios de modelo.
- CA-12: Las páginas interiores comienzan después de la altura de navegación más un margen móvil de `2rem`.
- CA-13: Desde tablet se recupera una altura de cabecera moderada sin volver a los valores originales.
- CA-14: Cada ruta pública renderiza un único canvas hexagonal fijo y no carga el fondo interior duplicado.

## Fuera de alcance

- Modificar modelos, migraciones, base de datos o Django Admin.
- Cambiar URLs o lógica de negocio.
- Crear un formulario de contacto.
- Inventar contenido, enlaces, imágenes o datos.
- Sustituir Django templates por una SPA.
- Migrar a Bootstrap 5, Tailwind u otro framework.
