# DelfoFolio

Portfolio personal y profesional de Delfín Rojas, desarrollado con Python y Django.

DelfoFolio es una aplicación web en evolución para presentar proyectos de desarrollo, dashboards de Power BI, tecnologías, formación y experiencia profesional.

**Portfolio en producción:** [delforojas.es](https://delforojas.es)

## 🌐 Demo

[https://delforojas.es](https://delforojas.es)

La aplicación se publica bajo un dominio propio y utiliza contenido administrable desde Django Admin.

## ✨ Qué encontrarás

- Proyectos web y dashboards Power BI separados por categoría.
- Catálogo visual de tecnologías.
- Datasets y recursos con enlaces y archivos multimedia.
- Cursos, formación académica y experiencia laboral.
- Página personal y canales de contacto profesional.
- Interfaz responsive con navegación compartida e intro de vídeo en la portada.

## 🛠️ Tecnología

- Python y Django 5.1.7.
- Templates Django con arquitectura MVT.
- HTML, CSS y JavaScript.
- Bootstrap, jQuery y Font Awesome incluidos en los assets del proyecto; p5.js cargado para el fondo visual.
- SQLite para el entorno local.
- Pillow y django-ckeditor para contenido multimedia y enriquecido.

La configuración de producción, el hosting y la gestión de contenido se documentan por separado. No se incluyen en este README valores sensibles ni una enumeración de tecnologías que solo aparecen en el catálogo visual del portfolio.

## 📚 Documentación técnica

| Área | Documento |
| --- | --- |
| Arquitectura Django y flujo MVT | [docs/arquitectura.md](docs/arquitectura.md) |
| Proyectos, dashboards y modelos de contenido | [docs/portfolio.md](docs/portfolio.md) |
| Administración y mantenimiento del contenido | [docs/gestion-de-contenido.md](docs/gestion-de-contenido.md) |
| Frontend, templates y assets | [docs/frontend.md](docs/frontend.md) |
| Configuración y prácticas de seguridad | [docs/seguridad.md](docs/seguridad.md) |
| Desarrollo local, tests y despliegue | [docs/desarrollo.md](docs/desarrollo.md) |
| Evolución del proyecto | [docs/evolucion.md](docs/evolucion.md) |
| Especificaciones de funcionalidades | [spec/README.md](spec/README.md) |

## 🚀 Inicio rápido

```bash
git clone https://github.com/Delforojas/delfofolio.git
cd delfofolio
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Sustituye el valor ficticio y exporta las variables según docs/desarrollo.md
python manage.py migrate
python manage.py runserver
```

El proyecto no carga `.env` automáticamente. Consulta [docs/desarrollo.md](docs/desarrollo.md) para configurar las variables en la sesión de shell antes de ejecutar Django.

## 👤 Autor

**Delfín Rojas**

- Portfolio: [delforojas.es](https://delforojas.es)
- GitHub: [Delforojas](https://github.com/Delforojas)
- LinkedIn: [delfinrojas](https://www.linkedin.com/in/delfinrojas)
