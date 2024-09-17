
# Hexagonal CQRS Backend

## Descripción

Este proyecto tiene como objetivo la creación de un backend con una arquitectura basada en Hexagonal Architecture (Arquitectura Hexagonal) y el patrón CQRS (Command Query Responsibility Segregation). El objetivo es organizar el código de manera limpia y estructurada, separando las responsabilidades de comandos y consultas, así como la capa de dominio, infraestructura y aplicación.

## Tecnologías usadas:

- **FastAPI** - Framework de Python para el desarrollo de APIs rápidas y sencillas.
- **SQLAlchemy** - ORM (Object-Relational Mapper) para manejar interacciones con la base de datos.
- **MySQL** - Base de datos relacional utilizada para almacenar los datos.
- **Docker** - Para contenedores y despliegue.
- **Pydantic** - Para validaciones y estructuración de datos.
- **Uvicorn** - Servidor ASGI para la ejecución del backend.

## Requisitos previos:

- **Python 3.8+**
- **MySQL** instalado y configurado en tu máquina.

## Instrucciones de Configuración

### Opción 1: Usando Docker

1. Clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/JorkDev/hexagonal_cqrs_backend
   cd hexagonal_cqrs_backend
   ```

2. Ejecuta el proyecto usando Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. La aplicación estará disponible en `http://localhost:8000`.

### Opción 2: Configuración manual

1. Clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/JorkDev/hexagonal_cqrs_backend
   cd hexagonal_cqrs_backend
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scriptsctivate
   ```

### Instalación de dependencias:

Primero, es necesario crear un entorno virtual en Python para aislar las dependencias del proyecto. Si no tienes `virtualenv` instalado, puedes instalarlo con:

```bash
pip install virtualenv
```

Luego, sigue los siguientes pasos:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Linux/Mac)
source venv/bin/activate

# Activar entorno virtual (Windows)
.env\Scriptsctivate

# Instalar las dependencias del proyecto
pip install -r requirements.txt
```

## Configuración de la Base de Datos:

1. Asegúrate de tener **MySQL** instalado en tu máquina.
2. Crea una base de datos llamada `hexagonal_cqrs_backend` con un usuario que tenga permisos de escritura y lectura.

```sql
CREATE DATABASE hexagonal_cqrs_backend;
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'new_password';
GRANT ALL PRIVILEGES ON hexagonal_cqrs_backend.* TO 'new_user'@'localhost';
FLUSH PRIVILEGES;
```

3. Verifica que la conexión a la base de datos en `main.py` esté correctamente configurada con los credenciales de MySQL:

```python
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://new_user:new_password@localhost/hexagonal_cqrs_backend"
```

## Cómo correr el proyecto:

### Opción 1: Localmente

1. Asegúrate de tener activado tu entorno virtual y que las dependencias estén instaladas.
2. Inicia la aplicación con **Uvicorn**:

```bash
uvicorn main:app --reload
```

Esto levantará el servidor en `http://127.0.0.1:8000/`.

### Opción 2: Usando Docker

Si prefieres usar Docker para correr el proyecto, puedes usar el siguiente `Dockerfile` incluido en el proyecto.

Para construir la imagen de Docker:

```bash
docker build -t hexagonal_cqrs_backend .
```

Para correr el contenedor:

```bash
docker run -p 8000:8000 hexagonal_cqrs_backend
```

## Rutas implementadas

1. **POST /register/**  
   Registro de un nuevo usuario.  
   Parámetros:  
   - `username` (str)
   - `email` (str)

   Ejemplo de solicitud:

   ```bash
   curl -X POST "http://127.0.0.1:8000/register/" -H "Content-Type: application/json" -d '{"username": "testuser", "email": "testuser@example.com"}'
   ```

2. **GET /user/{user_id}**  
   Obtener un usuario por su ID.

3. **GET /**  
   Página de bienvenida para verificar que el backend está funcionando.

## Cómo ejecutar los tests:

Se han implementado algunos tests básicos para validar las funcionalidades del backend. Para ejecutarlos, simplemente corre:

```bash
pytest
```

Esto ejecutará todos los tests dentro de la carpeta `tests/` y te mostrará los resultados.

## Conclusiones:

El proyecto ha sido desarrollado para demostrar los principios de la arquitectura hexagonal y CQRS. El uso de FastAPI y SQLAlchemy permite una implementación modular y escalable que facilita la separación de responsabilidades y la mantenibilidad del código. Este proyecto puede ser extendido para manejar más casos de uso como la autenticación, autorización, y otras operaciones de dominio complejas.

Agradecemos tu tiempo y estamos abiertos a cualquier consulta técnica adicional a través del contacto proporcionado.

![Vista Previa](https://i.imgur.com/kcMev97.png)
