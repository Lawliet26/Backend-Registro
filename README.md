# Backend Registro

Proyecto de backend en Django para la gestión de usuarios, registro y autenticación, pensado como base para pruebas de automatización y desarrollo de APIs REST. Utiliza PostgreSQL como base de datos y está configurado para trabajar con variables de entorno.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- **Python 3.12** o superior
- **PostgreSQL** (versión 12 o superior)
- **pip** y **pipenv** para la gestión de dependencias
- **Git** (para clonar el repositorio)

## Estructura del Proyecto

```
register-back/
├── apps/
│   └── register/
│       ├── api/
│       │   ├── serializers.py
│       │   ├── views.py
│       │   └── urls.py
│       ├── migrations/
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── registerback/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env (archivo requerido - ver configuración abajo)
├── manage.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Principales Características

- Registro de usuarios con roles personalizados (`usuario_final`, `productor`, `comerciante`).
- API RESTful usando Django REST Framework.
- Validación de contraseñas y términos.
- Soporte para CORS (peticiones desde frontend en React/Vite).
- Modelo de usuario personalizado (`User`).
- **Base de datos PostgreSQL** para persistencia de datos.
- **Configuración mediante variables de entorno** para mayor seguridad.

## Configuración de Base de Datos PostgreSQL

1. **Instala PostgreSQL:**
   - Descarga e instala PostgreSQL desde [postgresql.org](https://www.postgresql.org/download/)
   - Durante la instalación, recuerda la contraseña del usuario `postgres`

2. **Crea una base de datos para el proyecto:**
   ```sql
   -- Conecta a PostgreSQL como usuario postgres
   psql -U postgres
   
   -- Crea la base de datos
   CREATE DATABASE registro_db;
   
   -- Crea un usuario para el proyecto (opcional pero recomendado)
   CREATE USER registro_user WITH PASSWORD 'tu_contraseña_segura';
   
   -- Otorga permisos al usuario
   GRANT ALL PRIVILEGES ON DATABASE registro_db TO registro_user;
   
   -- Sal de psql
   \q
   ```

## Configuración del Archivo .env

**IMPORTANTE:** Crea un archivo `.env` en la raíz del proyecto (mismo nivel que `manage.py`) con la siguiente estructura:

```env
# Configuración de la Base de Datos PostgreSQL
DB_NAME=registro_db
DB_USER=registro_user
DB_PASSWORD=tu_contraseña_segura
DB_HOST=localhost
DB_PORT=5432

# Configuración de Django (opcional - para mayor seguridad)
# SECRET_KEY=tu_clave_secreta_django
# DEBUG=True
```

**Notas importantes sobre el .env:**
- Reemplaza `tu_contraseña_segura` con la contraseña que configuraste para PostgreSQL
- Si usas el usuario `postgres` directamente, cambia `DB_USER=postgres`
- Si PostgreSQL está en un puerto diferente, modifica `DB_PORT`
- El archivo `.env` **NO debe subirse a control de versiones** por seguridad

## Instalación y Ejecución

### 1. **Clona el repositorio:**
```bash
git clone <url-del-repo>
cd register-back
```

### 2. **Instala pipenv si no lo tienes:**
```bash
pip install pipenv
```

### 3. **Instala todas las dependencias del proyecto:**
```bash
pipenv install
pipenv shell
```
*Este comando instala automáticamente todas las dependencias especificadas en el `Pipfile`*

### 4. **Configura el archivo .env:**
- Crea el archivo `.env` en la raíz del proyecto
- Copia la estructura mostrada arriba y configura tus valores

### 5. **Aplica las migraciones:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Crea un superusuario (opcional pero recomendado):**
```bash
python manage.py createsuperuser
```

### 7. **Ejecuta el servidor:**
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## Endpoints Principales

- `POST /api/register/` — Registro de usuario
- `GET /admin/` — Panel de administración de Django
- `GET /` — Página de bienvenida del proyecto

## Dependencias Principales

El proyecto utiliza las siguientes dependencias (definidas en `Pipfile`):

- **Django** - Framework web principal
- **djangorestframework** - Para crear APIs REST
- **django-cors-headers** - Manejo de CORS para peticiones frontend
- **psycopg2-binary** - Conector para PostgreSQL
- **python-dotenv** - Carga de variables de entorno desde archivo .env
- **pipenv** - Gestión de dependencias y entornos virtuales

## Verificación de la Instalación

Para verificar que todo está funcionando correctamente:

1. **Verifica la conexión a la base de datos:**
   ```bash
   python manage.py dbshell
   ```
   Si se conecta sin errores, la configuración es correcta.

2. **Ejecuta las pruebas:**
   ```bash
   python manage.py test
   ```

3. **Accede al panel de administración:**
   - Ve a `http://127.0.0.1:8000/admin/`
   - Usa las credenciales del superusuario que creaste

## Solución de Problemas Comunes

### Error de conexión a PostgreSQL
- Verifica que PostgreSQL esté ejecutándose
- Confirma que los datos en el archivo `.env` sean correctos
- Asegúrate de que la base de datos existe

### Error "No module named psycopg2"
```bash
# Reinstala las dependencias del proyecto
pipenv install

# Si persiste el problema, instala manualmente:
pipenv install psycopg2-binary
```

### Error de migraciones
```bash
# Limpia y regenera las migraciones
python manage.py makemigrations --empty register
python manage.py makemigrations
python manage.py migrate
```

## Notas de Desarrollo

- El archivo `.env` debe estar en `.gitignore` para evitar subir credenciales
- El modelo de usuario personalizado requiere `AUTH_USER_MODEL = 'register.User'` en settings.py
- El backend está configurado para recibir peticiones desde `localhost:5173` (Vite) y `localhost:3000` (React)
- En producción, cambiar `DEBUG = False` y configurar `ALLOWED_HOSTS` apropiadamente

## Estructura de la Base de Datos

El proyecto utiliza un modelo de usuario personalizado con los siguientes roles:
- `usuario_final` - Usuario final del sistema
- `productor` - Usuario productor
- `comerciante` - Usuario comerciante

---

> Proyecto de prueba para verificar el funcionamiento de la automatización de n8n y la integración de APIs en Django con PostgreSQL.

## Información Adicional

- **Versión de Python requerida:** 3.12+
- **Base de datos:** PostgreSQL 12+
- **Framework:** Django 5.2.6+
- **Licencia:** [Especificar si aplica]

Para más información sobre el desarrollo o contribuciones, contacta al desarrollador del proyecto.
