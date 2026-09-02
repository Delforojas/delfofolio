# Frontend

La interfaz se construye con templates Django, sin frontend SPA ni sistema de build JavaScript.

## Templates

`core/templates/core/base.html` define el documento HTML, la navegación, el contenido principal, el footer y los scripts comunes. Las páginas específicas heredan ese layout mediante `{% extends %}`.

También se reutilizan parciales para:

- encabezados de página;
- enlaces sociales;
- listados de proyectos y dashboards.

## Estilos y componentes

- Bootstrap proporciona la cuadrícula, el menú responsive y componentes de interacción.
- `core/static/core/css/site.css` contiene la base visual actual.
- El proyecto conserva otros CSS históricos para páginas o efectos existentes.
- Font Awesome y `technology-icons.svg` proporcionan iconos.
- Las tarjetas de contenido utilizan imágenes responsive, texto alternativo y carga diferida cuando corresponde.

## JavaScript y vídeo

- jQuery y Bootstrap se cargan desde los assets incluidos en el proyecto.
- p5.js se utiliza para el fondo visual.
- `video-intro.js` controla la introducción de vídeo de la portada.
- El vídeo `core/static/core/logomotion-720p.mp4` se reproduce inicialmente sin sonido y en modo inline.

La navegación y los templates se han reorganizado para mantener una experiencia común en escritorio y dispositivos móviles.
