# Microservicio de Blacklist

El objetivo del microservicio de Blacklist es proporcionar una API robusta y segura para gestionar una lista negra de direcciones de correo electrónico. Este microservicio permite a las aplicaciones clientes agregar, consultar y eliminar direcciones de correo electrónico de la lista negra, asegurando que las direcciones bloqueadas no puedan interactuar con el sistema. Además, el microservicio valida las solicitudes entrantes y proporciona respuestas claras y detalladas en caso de errores, como campos faltantes o usuarios no encontrados.

## Estructura

La estructura de archivos del microservicio es la siguiente:

```
DEVOPS_08/
├── src/                        # Código fuente del microservicio
│   ├── blueprints/             # Contiene los blueprints de la aplicación Flask
│   │   ├── __init__.py
│   │   └── blacklist.py
│   ├── commands/               # Lógica de negocio organizada por comandos
│   │   ├── __init__.py
│   │   ├── base_command.py     # Clase base para los comandos
│   │   ├── create_blacklist.py
│   │   ├── get_blacklist_info.py
│   │   └── reset_database.py
│   ├── errors/               # Manejo de errores personalizados
│   │   ├── __init__.py
│   │   └── errors.py
│   ├── models/               # Modelos y esquemas de datos de usuario
│   │   ├── __init__.py
│   │   ├── model.py          # Definición de la tabla de blacklist
│   │   └── schemas.py        # Esquemas de serialización
│   ├── database.py           # configuración de la base de datos
│   └── main.py               # Punto de entrada de la aplicación
├── tests/                    # Pruebas unitarias para el microservicio
│   ├── blueprints/           # Pruebas para los blueprints
│   │   └── ...
│   ├── commands/             # Pruebas para los comandos
│   │   └── ...
│   └── conftest.py           # Archivo de configuración para pytest
├── Dockerfile                # Definición de la imagen Docker
├── Pipfile                   # Dependencias del proyecto
├── Pipfile.lock              # Versiones bloqueadas de dependencias
├── docker-compose.yml        # Archivo de despliegue usando Docker Compose
└── README.md                 # Documentación del microservicio

```

## Ejecución con compose

Para ejecutar el microservicio, sigue los pasos a continuación. Estos comandos te permitirán construir y ejecutar el contenedor Docker del microservicio en tu máquina local.

1. Asegurate de tener instalado Docker y Docker Compose en tu máquina.
2. Clona el repositorio del proyecto en tu máquina local.
3. Navega al directorio del reposotirio desde la terminal
4. Ejecuta el siguiente comando para construir y ejecutar el contenedor Docker del microservicio:

```bash
docker-compose up -d
```

5. Carga el archivo `Blacklist Service API.postman_collection.json` en Postman para probar los endpoints del microservicio.


## Otras Características (opcional)

Este proyecto de microservicio tiene las siguientes características adicionales que pueden ser útiles:

- **Persistencia en PostgreSQL:** El microservicio utiliza una base de datos PostgreSQL para almacenar y gestionar los datos de las publicaciones.
- **Manejo de Errores:** Implementa un manejo de errores robusto para asegurar respuestas claras y útiles a los usuarios finales y a otros servicios.
- **Despliegue en Docker:** El microservicio está configurado para ejecutarse en contenedores Docker, facilitando su despliegue en diferentes entornos.

