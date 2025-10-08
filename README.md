# Backend Registro

Proyecto de backend en Django para la gestión de usuarios, registro y autenticación, pensado como base para pruebas de automatización y desarrollo de APIs REST.

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
├── db.sqlite3
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

## Instalación y Ejecución

1. **Clona el repositorio:**
	```bash
	git clone <url-del-repo>
	cd register-back
	```

2. **Instala dependencias:**
	```bash
	pipenv install
	pipenv shell
	```

3. **Crea la base de datos y aplica migraciones:**
	```bash
	python manage.py makemigrations
	python manage.py migrate
	```

4. **Crea un superusuario (opcional):**
	```bash
	python manage.py createsuperuser
	```

5. **Ejecuta el servidor:**
	```bash
	python manage.py runserver
	```

## Endpoints Principales

- `POST /api/register/` — Registro de usuario
- `admin/` — Panel de administración de Django

## Dependencias principales

- Django
- djangorestframework
- django-cors-headers
- pipenv

## Notas de desarrollo

- El archivo `.gitignore` está configurado para ignorar archivos sensibles y entornos virtuales.
- El modelo de usuario personalizado requiere que `AUTH_USER_MODEL = 'register.User'` esté definido en `settings.py`.
- El backend está preparado para recibir peticiones desde `localhost:5173` (Vite) y `localhost:3000` (React).

---

> Proyecto de prueba para verificar el funcionamiento de la automatización de n8n y la integración de APIs en Django.

## Pruebas:
- Estas seran noificaciones de prueba
- Primera prueba falló - El webhook n8n no estaba escuchando
- Segunda prueba, funcionó  si estaba esuchando
- Tercera rueba, con flujo con http request por probar 
- Pruebas funcionando Descarga de de documentación pendiente
- Se realizaran pruebas para la segunda integración de flujo con Fong

- Pasos a realizar despues que quedan pendientes en la app es realizar el rolamiento de los usuarios y asiganr permisos 

- Cambio para agregar flujo alterno del proceso de documentación
- Prueba de plujo alterno 2