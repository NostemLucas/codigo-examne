# Inicio Rápido - Sistema de Florería

Guía rápida para ejecutar el proyecto en menos de 5 minutos.

## Requisitos Previos

- Python 3.11+
- MySQL instalado y en ejecución
- UV instalado

## Pasos Rápidos

### 1. Instalar dependencias

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

Editar `.env` con tus credenciales de MySQL:
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
# Integrante 1 - Categorías
git checkout -b modulo-categorias-tunombre

# Integrante 2 - Productos
git checkout -b modulo-productos-tunombre

# Integrante 3 - Pedidos
git checkout -b modulo-pedidos-tunombre
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

## Problemas Comunes

### Error de conexión MySQL
- Verificar que MySQL esté corriendo
- Verificar credenciales en .env
- Verificar que la base de datos exista

### Error de importación
- Verificar que estás en el entorno virtual: `source .venv/bin/activate`
- Reinstalar dependencias: `uv sync`

### Error de permisos
- Linux/Mac: Verificar permisos de carpeta uploads: `chmod 755 app/static/uploads`

### Puerto en uso
- Cambiar puerto: `flask run --port=5001`

## Desarrollo

### Ejecutar en modo debug

```bash
export FLASK_ENV=development  # Linux/Mac
set FLASK_ENV=development  # Windows

flask run --debug
```

### Ver logs

Los logs se muestran en la consola donde ejecutaste `flask run`.

## Testing Manual

1. **Auth**: Registro, login, logout
2. **Categorías**: Crear, editar, eliminar, listar
3. **Productos**: Crear con imagen, editar, eliminar
4. **Pedidos**: Crear, ver, cambiar estado

## Siguiente Paso

Lee el [README.md](README.md) completo para documentación detallada.

## Soporte

Si encuentras problemas, revisa:
1. Los logs en la consola
2. El README.md completo
3. La documentación de cada módulo
