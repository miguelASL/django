# django
## Crear un proyecto
```bash
django-admin startproject "hola_mundo"
```
MTV -> Modelo, Template, Vista

## Estructura del proyecto

El proyecto `holamundo` tiene la siguiente estructura de directorios y archivos:

```
holamundo/
    holamundo/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    manage.py
    README.md
```

### Descripción de los archivos

- `holamundo/manage.py`: Es una utilidad de línea de comandos que permite interactuar con este proyecto Django de varias maneras. Puedes usarlo para iniciar el servidor de desarrollo, sincronizar la base de datos, crear nuevas aplicaciones, entre otras tareas administrativas.

- `holamundo/holamundo/__init__.py`: Un archivo vacío que indica a Python que este directorio debe ser considerado como un paquete.

- `holamundo/holamundo/asgi.py`: Configuración para el servidor de aplicaciones ASGI (Asynchronous Server Gateway Interface). ASGI es el sucesor de WSGI y permite manejar aplicaciones asíncronas.

- `holamundo/holamundo/settings.py`: Contiene la configuración del proyecto Django, incluyendo la configuración de la base de datos, aplicaciones instaladas, middleware, y otras configuraciones globales.

- `holamundo/holamundo/urls.py`: Define las rutas URL para el proyecto. Aquí se mapean las URLs a las vistas correspondientes.

- `holamundo/holamundo/wsgi.py`: Configuración para el servidor de aplicaciones WSGI (Web Server Gateway Interface). WSGI es una especificación para la comunicación entre servidores web y aplicaciones web en Python.

- `README.md`: Este archivo de documentación que estás leyendo.
