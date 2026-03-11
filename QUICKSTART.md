# Inicio Rápido - Sistema de Florería

Guía rápida para ejecutar el proyecto en menos de 5 minutos.

## Requisitos Previos

- Python 3.11+
- MySQL instalado y en ejecución
- UV instalado

## Pasos Rápidos

uv gestiona las versiones de python para instalarlo

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

posterior para instalar las dependencias del proyecto

```bash
uv sync
```

### 2. Crear base de datos

```sql
mysql -u root -p
CREATE DATABASE floreria_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

### 3. Configurar .env

```bash
cp .env.example .env
```

Editar `.env` con las credenciales de MySQL:

```env
DATABASE_URL=mysql+pymysql://root:tu_password@localhost/floreria_db
```

### 4. Inicializar base de datos

```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
# o .venv\Scripts\activate en Windows

# Inicializar migraciones
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Cargar datos iniciales
flask init-db

# Crear admin
flask create-admin
# Usuario: admin
# Email: admin@floreria.com
# Password: admin123
# Nombre: Administrador
```

### 5. Ejecutar aplicación

```bash
python main.py
```

Abrir navegador en: http://localhost:5000

## Usuarios de Prueba

Después de ejecutar `flask create-admin`:

**Admin**

- Usuario: admin
- Password: admin123
- Acceso total

**Crear vendedor** (en flask shell):

```python
flask shell
>>> from app.models import Usuario
>>> from app.extensions import db
>>> vendedor = Usuario(username='vendedor', email='vendedor@floreria.com', nombre_completo='Vendedor Test', rol='vendedor')
>>> vendedor.set_password('vendedor123')
>>> db.session.add(vendedor)
>>> db.session.commit()
```

**Cliente** (registrarse desde la web):

- Ir a /auth/registro
- Completar formulario

## Probar Funcionalidades

### Como Admin:

1. Login con admin/admin123
2. Ir a /admin/ para panel de administración
3. Crear categorías desde /categorias/crear
4. Crear productos desde /productos/crear (con imagen)

### Como Cliente:

1. Registrarse en /auth/registro
2. Ver productos en /productos
3. Crear pedido en /pedidos/crear

## Estructura de Ramas

```bash
completar
```

## Comandos Útiles

```bash
# Shell interactivo con modelos
flask shell

# Ver rutas
flask routes

# Crear migración
flask db migrate -m "Descripción"

# Aplicar migraciones
flask db upgrade

# Revertir migración
flask db downgrade
```
