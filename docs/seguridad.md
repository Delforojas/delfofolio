# Configuración y seguridad

La configuración separa los valores sensibles del código fuente.

## Variables de entorno

`webpersonal/settings.py` utiliza:

- `DJANGO_SECRET_KEY`: clave criptográfica obligatoria, no incluida en Git.
- `DJANGO_DEBUG`: activa debug mediante una lista de valores reconocidos; su valor por defecto es `False`.
- `DJANGO_ALLOWED_HOSTS`: lista de hosts separada por comas, con los dominios públicos como valor por defecto.

`.env.example` documenta estas variables con valores ficticios. El proyecto no carga archivos `.env` automáticamente; las variables deben estar exportadas en el entorno de ejecución.

## Archivos locales

`.gitignore` excluye archivos de entorno, bases SQLite y sus ficheros auxiliares, bytecode, cachés, logs, temporales, entornos virtuales, `.DS_Store` y configuración local de IDEs.

La base de datos local puede existir en el equipo de desarrollo para ejecutar la aplicación, pero no debe versionarse ni utilizarse como mecanismo de distribución de datos.

## Alcance

Estas decisiones reducen la publicación accidental de secretos y datos locales. No sustituyen la revisión de cambios, la rotación de credenciales ni las comprobaciones de seguridad del entorno de producción.
