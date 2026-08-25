# Plan de la feature 009: Modernización visual y responsive

## Estado

Aprobado, implementado y validado técnicamente.

## Dirección técnica

Se mantendrá Bootstrap como base, actualizando los assets locales de 4.0 beta a 4.6.2. Los estilos propios dispersos se reemplazarán en la carga por `core/css/site.css`, sin borrar inicialmente los archivos heredados.

## Fases

### 1. Sistema global

- Definir tokens de color, tipografía, espaciado, radios y contenedores.
- Modernizar navegación, dropdown, foco, skip link, `main` y footer.
- Crear parciales para cabecera interior y enlaces sociales.

### 2. Contenido estático

- Migrar Portada, Acerca de y Contacto.
- Conservar todos los textos y destinos existentes.

### 3. Listados administrables

- Migrar Datasets, Cursos, Formación académica y Experiencia laboral.
- Corregir grids, imágenes opcionales, acciones y estados vacíos.

### 4. Proyectos

- Modernizar el parcial compartido por Portfolio y Dashboards.
- Mantener filtros, datos y enlaces actuales.

### 5. Rendimiento visual

- Eliminar de la carga los scripts de hover duplicados.
- Optimizar el fondo p5 sin cambiar su identidad.
- Montar un único canvas fijo en el layout global y retirar las instancias locales de cada cabecera.
- Mantener cabeceras y footer semitransparentes para conservar continuidad y legibilidad.

### 6. Validación

- Añadir pruebas de renderizado y estados opcionales.
- Ejecutar checks y tests Django.
- Validar rutas, breakpoints, teclado, foco, movimiento reducido y overflow.

## Archivos nuevos

- `core/static/core/css/site.css`
- `core/templates/core/_page_header.html`
- `core/templates/core/_social_links.html`

## Restricciones

- Sin cambios de modelos, datos, migraciones, URLs o vistas de negocio.
- Sin edición manual de `staticfiles/`.
- Sin contenido ficticio.
- Sin dependencias Python o framework frontend nuevo.

## Verificación técnica

```bash
python manage.py makemigrations --check --dry-run
python manage.py check
python manage.py test
```

Las rutas públicas se comprobarán también con el cliente de pruebas de Django.

## Ajuste de densidad vertical

La revisión visual posterior reduce de forma global la altura y el padding de `.page-hero`, el padding de `.page-section` y los espacios internos de las tarjetas. Los valores base priorizan móvil y un breakpoint desde `48rem` recupera una composición más amplia para tablet y escritorio.

No se introducen excepciones por vista. Portada conserva su hero de pantalla completa y solo equilibra el padding respecto a la navbar.

## Fondo hexagonal global

El canvas p5 se monta una sola vez en `core/base.html` y usa `fondo.js` para cubrir el viewport. Su posición fija mantiene el patrón continuo durante el scroll y evita crear un canvas y cargar scripts específicos en cada vista. Las tarjetas conservan sus superficies y las capas estructurales usan transparencia controlada para no comprometer el contraste.
