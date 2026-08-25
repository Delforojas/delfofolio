# Documentación SDD del proyecto

Esta carpeta recoge la documentación del proyecto siguiendo una estructura de Spec Driven Development (SDD), basada únicamente en lo que existe en el repositorio actual.

## Objetivo de esta documentación

Documentar:

- el propósito del proyecto
- la tecnología realmente usada
- la arquitectura observada
- las funcionalidades ya implementadas
- la forma actual de ejecución y verificación
- las limitaciones y supuestos que no pueden demostrarse a partir del código

## Cómo usar esta documentación

1. Empieza por la constitución:
   - `spec/constitution/mission.md`
   - `spec/constitution/tech-stack.md`
   - `spec/constitution/roadmap.md`
2. Revisa las features concretas dentro de `spec/features/`.
3. Usa cada feature para entender:
   - qué hace actualmente
   - cómo está implementada
   - qué tareas son necesarias para reproducir o verificar la funcionalidad

## Estructura

```text
spec/
├── README.md
├── constitution/
│   ├── mission.md
│   ├── tech-stack.md
│   └── roadmap.md
└── features/
    ├── 001-home/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 002-about-contact/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 003-portfolio/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 004-datasets/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 005-formacion-cursos/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 006-formacion-academica/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 007-experiencia-laboral/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 008-power-bi/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    ├── 009-modernizacion-visual-responsive/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    └── 010-tecnologias/
        ├── spec.md
        ├── plan.md
        └── tasks.md
```

## Principio de documentación

Esta documentación no inventa requisitos, features, comandos ni tecnologías que no aparezcan en el repositorio.

Cuando algo no se puede deducir con confianza, se indica explícitamente como una limitación del proyecto actual.

## Fuentes de referencia del repositorio

Las evidencias principales han sido:

- `requirements.txt`
- `manage.py`
- `webpersonal/settings.py`
- `webpersonal/urls.py`
- `core/views.py`
- `portfolio/models.py`
- `formacion/models.py`
- `laboral/models.py`
- `dataset/models.py`
- plantillas dentro de `core/templates/`, `portfolio/templates/`, `formacion/templates/`, `laboral/templates/` y `dataset/templates/`

## Alcance

La documentación describe el proyecto tal y como está implementado ahora mismo en el código actual. No añade nuevas arquitecturas ni nuevas funcionalidades fuera del alcance observable en el repositorio.
