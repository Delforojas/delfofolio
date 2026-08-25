# Feature 010: Tecnologías

## Estado

Implementada y validada técnica y visualmente en Safari para móvil, tablet y escritorio.

## Descripción

Incorporar "Tecnologías" como una sección principal e independiente del portfolio. La página muestra las tecnologías, lenguajes y herramientas aprobadas por el usuario, agrupadas por categorías y representadas mediante un icono local y su nombre.

## Objetivo

Permitir que los visitantes conozcan de forma visual las capacidades técnicas del autor desde una ruta y una entrada propias en la navegación principal, sin crear modelos, migraciones ni gestión adicional en Django Admin.

## Catálogo aprobado

### Lenguajes y Frameworks

- Python
- Django
- JavaScript
- TypeScript
- PHP
- Symfony
- Angular
- HTML5
- CSS3

### Frontend y Diseño

- Bootstrap

### Datos y Business Intelligence

- SQL
- Power BI
- Pandas
- NumPy
- Matplotlib
- Power Query
- DAX
- Anaconda
- Scikit-learn

### Herramientas y Entornos

- Git
- GitHub
- Docker
- Visual Studio Code
- Postman

## Historias de usuario

### US1. Acceder a Tecnologías

Como visitante, quiero encontrar "Tecnologías" después de "Acerca de" en el menú principal para consultar directamente las capacidades técnicas del autor.

### US2. Explorar por categorías

Como visitante, quiero que las tecnologías estén agrupadas por ámbito para comprender el perfil técnico con rapidez.

### US3. Reconocer visualmente cada tecnología

Como visitante, quiero ver un icono consistente y el nombre de cada tecnología para identificarla sin depender únicamente del logo.

## Requisitos funcionales

- RF-01: Debe existir una ruta pública `/tecnologias/` con nombre `tecnologias`.
- RF-02: La navegación debe mostrar "Tecnologías" inmediatamente después de "Acerca de".
- RF-03: La página debe usar una vista funcional de `core` y el template `core/tecnologias.html`.
- RF-04: El catálogo debe almacenarse como una estructura Python ordenada dentro de `core`.
- RF-05: Solo deben mostrarse las 24 tecnologías aprobadas.
- RF-06: Las tecnologías deben conservar las cuatro categorías y el orden aprobado.
- RF-07: Cada tecnología debe mostrar un icono y su nombre visible.
- RF-08: Los iconos deben cargarse desde un sprite SVG local.
- RF-09: No deben realizarse peticiones externas para renderizar iconos.
- RF-10: La navegación debe marcar la página activa con `aria-current="page"`.

## Requisitos visuales y responsive

- RV-01: Reutilizar el fondo global, paleta, tipografías, espaciado y superficies de la web actual.
- RV-02: Cada categoría debe disponer de un encabezado y un grid independiente.
- RV-03: Las tarjetas deben mantener iconos con dimensiones visuales consistentes.
- RV-04: El hover debe ser sutil y no sugerir una acción inexistente.
- RV-05: Los iconos deben usar colores de marca directamente sobre las tarjetas, sin fondos ni marcos propios; SQL y DAX usan colores semánticos documentados.
- RSP-01: El grid debe mostrar dos columnas en móvil y aumentar progresivamente en tablet y escritorio.
- RSP-02: Ninguna tarjeta, nombre o categoría debe provocar overflow horizontal desde 320 px.
- RSP-03: La navegación debe permanecer utilizable con el nuevo enlace en todos sus estados.

## Accesibilidad

- A11Y-01: Cada categoría debe estar identificada mediante un encabezado asociado.
- A11Y-02: Los iconos deben ser decorativos porque el nombre ya comunica la tecnología.
- A11Y-03: El orden de lectura debe coincidir con el orden visual.
- A11Y-04: Los efectos visuales deben respetar `prefers-reduced-motion`.
- A11Y-05: El contraste de nombres, tarjetas y estados hover debe mantener el sistema vigente.

## Fuentes de iconos aprobadas

- Simple Icons, CC0 1.0: Python, Django, JavaScript, TypeScript, PHP, Symfony, Angular, HTML5, CSS, Bootstrap, Pandas, NumPy, Anaconda, scikit-learn, Git, GitHub, Docker y Postman.
- Devicon, licencia MIT: Matplotlib y Visual Studio Code.
- Microsoft Power BI Icons, licencia CC BY 4.0: SQL Query, Power BI, Power Query y Function.
- El símbolo CSS se presenta con el nombre visible "CSS3".
- El símbolo Function se presenta con el nombre visible "DAX" como alternativa semántica aprobada, ya que no existe un logo DAX específico en los catálogos revisados.
- Angular y Symfony conservan los colores de catálogo solicitados y aplican inversión visual para mantener contraste sobre el fondo oscuro.

## Requisitos técnicos

- RNF-01: No crear una app Django adicional.
- RNF-02: No crear ni modificar modelos, Django Admin o migraciones.
- RNF-03: No añadir dependencias Python o frontend.
- RNF-04: No modificar datos persistentes ni `staticfiles/`.
- RNF-05: Mantener Django templates y el layout compartido actual.
- RNF-06: Documentar la procedencia y licencia de los símbolos incluidos en el sprite.

## Criterios de aceptación

- CA-01: `/tecnologias/` responde con estado 200 y usa `core/tecnologias.html`.
- CA-02: Tecnologías aparece después de Acerca de en la navegación.
- CA-03: La navegación marca Tecnologías como página actual.
- CA-04: Se muestran cuatro categorías y exactamente 24 tecnologías.
- CA-05: Cada tecnología muestra un icono local y un nombre visible.
- CA-06: Todos los identificadores usados por el catálogo existen en el sprite.
- CA-07: La página no contiene URLs externas para cargar iconos.
- CA-08: El grid se adapta a móvil, tablet, escritorio y pantallas grandes sin overflow.
- CA-09: El layout global, el fondo y el footer se mantienen sin cambios funcionales.
- CA-10: No se generan cambios de modelo ni migraciones.
- CA-11: `python manage.py check` y `python manage.py test` finalizan sin errores propios de la feature.

## Fuera de alcance

- Gestionar tecnologías desde Django Admin.
- Crear relaciones entre tecnologías y proyectos.
- Añadir niveles, porcentajes o años de experiencia.
- Convertir las tarjetas en enlaces externos.
- Añadir filtros, búsquedas o animaciones complejas.
- Incorporar tecnologías no aprobadas.
