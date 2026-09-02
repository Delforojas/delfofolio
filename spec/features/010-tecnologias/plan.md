# Plan de la feature 010: Tecnologías

## Estado

Plan implementado y validado técnica y visualmente.

## Decisiones de arquitectura

### Dominio y almacenamiento

Tecnologías se implementará en `core` porque es una página informativa con un catálogo pequeño y estable. Una constante Python ordenada almacenará categorías y elementos, y la vista la entregará al template.

No se crearán app, modelo, Admin, migración ni datos persistentes.

### Ruta y navegación

`webpersonal/urls.py` publicará `/tecnologias/` con nombre `tecnologias`. `core/templates/core/base.html` añadirá el enlace inmediatamente después de Acerca de y aplicará el patrón actual de estado activo y `aria-current`.

### Vista y template

`core.views.tecnologias` renderizará `core/tecnologias.html` con `technology_categories`. El template heredará de `core/base.html`, reutilizará `core/_page_header.html` y recorrerá la estructura sin duplicar el marcado de categorías o tarjetas.

### Presentación

`core/static/core/css/site.css` incorporará clases específicas para categorías, grid, tarjetas, iconos y nombres. La cuadrícula será mobile-first y usará `minmax(0, 1fr)` para evitar overflow.

Distribución prevista:

- Móvil: 2 columnas.
- Móvil amplio: 3 columnas.
- Tablet: 4 columnas.
- Escritorio: 5 columnas.
- Pantalla grande: 6 columnas.

### Iconos

Los 24 símbolos se integrarán en `core/static/core/img/technology-icons.svg`. El template usará elementos SVG decorativos con referencias locales mediante `use`.

Fuentes verificadas y aprobadas:

- Simple Icons bajo CC0 1.0.
- Devicon bajo licencia MIT.
- Microsoft Power BI Icons bajo CC BY 4.0.

Se añadirá un aviso local con la relación de símbolos, fuentes, licencias y equivalencias. No se usarán CDNs ni URLs externas durante el renderizado.

## Archivos nuevos

- `core/templates/core/tecnologias.html`
- `core/static/core/img/technology-icons.svg`
- `core/static/core/img/technology-icons-NOTICE.md`
- `spec/features/010-tecnologias/spec.md`
- `spec/features/010-tecnologias/plan.md`
- `spec/features/010-tecnologias/tasks.md`

## Archivos modificados

- `core/views.py`
- `webpersonal/urls.py`
- `core/templates/core/base.html`
- `core/static/core/css/site.css`
- `core/tests.py`
- `spec/README.md`
- `spec/constitution/mission.md`
- `spec/constitution/roadmap.md`

## Archivos sin cambios

- `core/models.py`
- `core/admin.py`
- `webpersonal/settings.py`
- `requirements.txt`
- `db.sqlite3`
- `staticfiles/`

## Estrategia de pruebas

- Comprobar la resolución y respuesta de `/tecnologias/`.
- Comprobar el template y el contexto entregado por la vista.
- Comprobar categorías, orden y total de tecnologías.
- Comprobar el orden Acerca de > Tecnologías > Datasets en la navegación.
- Comprobar estado activo y `aria-current`.
- Comprobar que cada símbolo referenciado existe en el sprite.
- Comprobar que el template no carga iconos desde URLs externas.
- Revisar responsive en móvil, tablet y escritorio.

## Verificación

```bash
python manage.py makemigrations --check --dry-run
python manage.py check
python manage.py test
```

La ruta se comprobará también mediante el cliente Django y la presentación con un navegador en viewports representativos.

## Resultado técnico

La ruta, el catálogo, la navegación, el sprite y los breakpoints responsive están implementados. Las comprobaciones automáticas validan los 24 símbolos locales, la ausencia de cargas externas de iconos, el estado activo y la estructura mobile-first.

La revisión visual automatizada se completó con SafariDriver en 390 px, 768 px y 1440 px. No se detectó overflow horizontal, las tarjetas permanecen dentro del viewport, la navegación cambia correctamente entre modo colapsado y expandido, y los iconos se renderizan con tamaño consistente. Durante la revisión se corrigió el icono de Power BI para evitar gradientes incompatibles con referencias externas del sprite en Safari.

La ampliación a 24 tecnologías se verificó de nuevo en Safari. Angular, PHP, TypeScript, Symfony, Anaconda y Scikit-learn resuelven símbolos locales de 56 x 56 px; Angular y Symfony aplican inversión visual para conservar contraste sobre el fondo oscuro.
