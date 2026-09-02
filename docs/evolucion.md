# Evolución del proyecto

La evolución de DelfoFolio se puede seguir en el código, las migraciones y la documentación de `spec/`.

## Cambios observables

- La web personal inicial se organizó en apps Django por área de contenido.
- El portfolio incorporó categorías para distinguir proyectos generales y Power BI.
- Dashboards pasó a tener ruta, vista y página propias reutilizando el modelo `Project`.
- Se añadió una sección visual de tecnologías con un catálogo estático e iconos locales.
- El layout público se refactorizó alrededor de templates compartidos, parciales y estilos responsive.
- La portada incorporó una introducción de vídeo.
- Los templates añadieron mejoras de navegación, accesibilidad, estados vacíos, enlaces seguros y carga de imágenes.
- La aplicación se publicó bajo el dominio `delforojas.es`.
- La configuración sensible se separó mediante variables de entorno y el historial Git se saneó antes de la publicación pública.

## Documentación del cambio

La carpeta `spec/` acompaña esta evolución con una constitution del proyecto y documentos `spec.md`, `plan.md` y `tasks.md` por feature. Se utiliza como documentación técnica del trabajo realizado, no como una garantía de que todos los cambios históricos hayan seguido exactamente el mismo proceso.
