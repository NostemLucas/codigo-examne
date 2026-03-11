# Sistema de Florería - Ventas de Flores y Plantas

Sistema web de gestión de ventas de flores y plantas desarrollado con Flask, SQLAlchemy, Pydantic y MySQL.

## Integrantes del Equipo

- **Integrante 1**: Módulo de Categorías
  - Rama: `modulo-categorias-nombre_estudiante`
- **Integrante 2**: Módulo de Productos con subida de imágenes
  - Rama: `modulo-productos-nombre_estudiante`
- **Integrante 3**: Módulo de Pedidos/Ventas
  - Rama: `modulo-pedidos-nombre_estudiante`

## Características Principales

### 1. Autenticación y Roles

- **Registro de usuarios** con validaciones (Pydantic)
- **Login/Logout** con Flask-Login
- **Hash de contraseñas** con Werkzeug
- **3 Roles implementados**:
  - `admin`: Acceso total al sistema y panel de administración
  - `vendedor`: Gestión de categorías, productos y pedidos
  - `cliente`: Visualización de productos y creación de pedidos
- **Protección de rutas** por rol con decoradores personalizados
- **Restricción de vistas** según rol del usuario

### 2. Base de Datos (MySQL)

#### Modelos implementados (5 tablas):

1. **usuarios**: Gestión de usuarios con roles
2. **categorias**: Categorías de productos (Rosas, Orquídeas, Plantas, etc.)
3. **productos**: Productos con imagen, precio, stock y SKU
4. **pedidos**: Pedidos con estado, totales y datos de entrega
5. **detalles_pedido**: Ítems de cada pedido

#### Relaciones:
- Usuario → Pedidos (1:N)
- Categoría → Productos (1:N)
- Producto → DetallesPedido (1:N)
- Pedido → DetallesPedido (1:N)

### 3. Módulos CRUD

#### Módulo 1: Categorías (Integrante 1)
**Ubicación**: `app/categorias/`

**Funcionalidades**:
- ✅ Crear categorías con validación Pydantic
- ✅ Listar categorías con búsqueda y filtros
- ✅ Ver detalle de categoría con productos asociados
- ✅ Editar categorías
- ✅ Eliminar categorías (validando productos asociados)
- ✅ Activar/Desactivar categorías
- ✅ Generación automática de slug único

**Validaciones**:
- Nombre mínimo 3 caracteres
- Descripción máximo 500 caracteres
- Slug único generado automáticamente

#### Módulo 2: Productos (Integrante 2)
**Ubicación**: `app/productos/`

**Funcionalidades**:
- ✅ Crear productos con subida de imagen
- ✅ Listar productos con búsqueda avanzada y filtros
- ✅ Ver detalle de producto con relacionados
- ✅ Editar productos y actualizar imagen
- ✅ Eliminar productos y su imagen
- ✅ Marcar productos como destacados
- ✅ Generación automática de SKU
- ✅ **Subida y optimización de imágenes** (RETO ADICIONAL)

**Validaciones**:
- Nombre mínimo 3 caracteres
- Precio mayor a 0, máximo $9,999,999.99
- Stock no negativo, máximo 999,999
- SKU único alfanumérico
- Imágenes: PNG, JPG, JPEG, GIF, WEBP
- Tamaño máximo: 16MB
- Optimización automática a 1200x1200px

#### Módulo 3: Pedidos (Integrante 3)
**Ubicación**: `app/pedidos/`

**Funcionalidades**:
- ✅ Crear pedidos con múltiples productos
- ✅ Listar pedidos (clientes ven solo los suyos)
- ✅ Ver detalle de pedido
- ✅ Editar pedidos (solo vendedores)
- ✅ Cancelar pedidos con devolución de stock
- ✅ Cambiar estado del pedido (vendedores)
- ✅ Validación de stock antes de crear pedido
- ✅ Generación automática de número de pedido

**Estados de pedido**:
- `pendiente`: Pedido creado
- `procesando`: En preparación
- `enviado`: En camino
- `entregado`: Entregado al cliente
- `cancelado`: Cancelado (devuelve stock)

**Validaciones**:
- Dirección mínimo 10 caracteres
- Teléfono con al menos un dígito
- Al menos un producto en el pedido
- Validación de stock disponible
- No permitir productos duplicados
- Transiciones de estado válidas

### 4. Flask-Admin

**Panel de administración** con acceso restringido solo para administradores:
- Gestión completa de usuarios
- Gestión de categorías, productos y pedidos
- Vistas personalizadas con `SecureModelView`
- Redirección a login si no tiene permisos

**Acceso**: `/admin/`

### 5. RETO ADICIONAL: Subida de Imágenes

**Implementación**: `app/productos/utils.py`

**Características**:
- ✅ Subida de imágenes para productos
- ✅ Validación de extensiones permitidas
- ✅ Validación de tamaño máximo (16MB)
- ✅ Generación de nombres únicos (UUID)
- ✅ **Optimización con Pillow**:
  - Redimensionamiento automático a 1200x1200px
  - Compresión JPEG con calidad 85%
  - Conversión de PNG/transparencia a JPG
  - Reducción de tamaño de archivo
- ✅ Eliminación segura de imágenes antiguas
- ✅ Carpeta organizada: `app/static/uploads/productos/`

**Aprendizajes**:
- Manejo de FileStorage de Flask
- Procesamiento de imágenes con PIL/Pillow
- Optimización de almacenamiento
- Seguridad en subida de archivos
- Generación de thumbnails automáticos

## Tecnologías Utilizadas

- **Backend**: Flask 3.0
- **Validación**: Pydantic 2.5
- **ORM**: SQLAlchemy 2.0 con Flask-SQLAlchemy
- **Base de Datos**: MySQL con PyMySQL
- **Autenticación**: Flask-Login
- **Migraciones**: Flask-Migrate (Alembic)
- **Administración**: Flask-Admin
- **Procesamiento de Imágenes**: Pillow
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Gestión de Paquetes**: UV (ultrafast package manager)

## Estructura del Proyecto

```
examen/
├── app/
│   ├── __init__.py              # App Factory
│   ├── config.py                # Configuraciones
│   ├── extensions.py            # Extensiones Flask
│   ├── models.py                # Modelos SQLAlchemy
│   ├── views.py                 # Vistas principales
│   ├── admin_views.py           # Vistas Flask-Admin
│   ├── commands.py              # Comandos CLI
│   ├── auth/                    # Módulo de Autenticación
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── decorators.py
│   ├── categorias/              # Módulo de Categorías (Integrante 1)
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── productos/               # Módulo de Productos (Integrante 2)
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── utils.py             # Utilidades para imágenes
│   ├── pedidos/                 # Módulo de Pedidos (Integrante 3)
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── templates/               # Templates Jinja2
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── auth/
│   │   ├── categorias/
│   │   ├── productos/
│   │   └── pedidos/
│   └── static/                  # Archivos estáticos
│       ├── css/
│       ├── js/
│       ├── images/
│       └── uploads/
│           └── productos/       # Imágenes de productos
├── migrations/                  # Migraciones de Alembic
├── main.py                      # Punto de entrada
├── pyproject.toml              # Dependencias (UV)
├── .env.example                # Variables de entorno ejemplo
├── .gitignore
└── README.md
```

## Instalación y Configuración

### Prerrequisitos

- Python 3.11+
- MySQL 8.0+
- UV (package manager)

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/examen.git
cd examen
```

### 2. Instalar UV (si no lo tienes)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Crear entorno virtual e instalar dependencias

```bash
uv sync
```

### 4. Configurar base de datos

Crear base de datos en MySQL:

```sql
CREATE DATABASE floreria_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Configurar variables de entorno

Copiar `.env.example` a `.env` y configurar:

```bash
cp .env.example .env
```

Editar `.env`:

```env
SECRET_KEY=tu-clave-secreta-super-segura
DATABASE_URL=mysql+pymysql://usuario:password@localhost/floreria_db
```

### 6. Inicializar base de datos

```bash
# Activar entorno virtual
source .venv/bin/activate  # Linux/Mac
# o
.venv\Scripts\activate  # Windows

# Crear migraciones
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Inicializar con datos de prueba
flask init-db

# Crear usuario administrador
flask create-admin
```

### 7. Ejecutar aplicación

```bash
flask run
# o
python main.py
```

La aplicación estará disponible en: `http://localhost:5000`

## Flujo de Trabajo con Git

### Ramas del proyecto

```
master (o main)          # Rama principal protegida
├── modulo-categorias-nombre1
├── modulo-productos-nombre2
└── modulo-pedidos-nombre3
```

### Workflow para cada integrante

#### 1. Crear y cambiar a tu rama

```bash
# Integrante 1
git checkout -b modulo-categorias-juan

# Integrante 2
git checkout -b modulo-productos-maria

# Integrante 3
git checkout -b modulo-pedidos-pedro
```

#### 2. Trabajar en tu módulo

```bash
# Hacer cambios en tu módulo
# ...

# Agregar cambios
git add app/categorias/  # o productos/ o pedidos/
git add app/templates/categorias/  # si aplica

# Commit con mensaje descriptivo
git commit -m "feat(categorias): agregar búsqueda y filtros"
```

#### 3. Subir cambios a tu rama

```bash
git push origin modulo-categorias-juan
```

#### 4. Crear Pull Request

1. Ir a GitHub
2. Crear Pull Request desde tu rama hacia `master`
3. Describir los cambios realizados
4. Solicitar revisión de compañeros
5. Esperar aprobación y merge

### Comandos útiles

```bash
# Ver estado
git status

# Ver ramas
git branch

# Cambiar de rama
git checkout nombre-rama

# Actualizar tu rama con master
git checkout master
git pull origin master
git checkout tu-rama
git merge master

# Ver historial
git log --oneline --graph --all
```

## Comandos CLI Personalizados

```bash
# Inicializar base de datos con categorías de ejemplo
flask init-db

# Crear usuario administrador
flask create-admin

# Abrir shell con contexto (modelos disponibles)
flask shell

# Crear migración
flask db migrate -m "Descripción"

# Aplicar migraciones
flask db upgrade

# Ejecutar aplicación
flask run
```

## Testing

### Crear datos de prueba

```python
# En flask shell
flask shell

>>> # Crear categoría
>>> cat = Categoria(nombre="Rosas", descripcion="Rosas hermosas", slug="rosas")
>>> db.session.add(cat)
>>> db.session.commit()

>>> # Crear producto
>>> prod = Producto(
...     nombre="Rosa Roja",
...     descripcion="Rosa roja premium",
...     precio=15.99,
...     stock=100,
...     sku="FLO-12345",
...     categoria_id=cat.id
... )
>>> db.session.add(prod)
>>> db.session.commit()
```

## Usuarios de Prueba

Después de ejecutar `flask create-admin`, puedes crear usuarios de prueba:

```python
# Admin
username: admin
email: admin@floreria.com
password: admin123
rol: admin

# Vendedor (crear manualmente)
username: vendedor
email: vendedor@floreria.com
password: vendedor123
rol: vendedor

# Cliente (registro público)
username: cliente
email: cliente@floreria.com
password: cliente123
rol: cliente
```

## Rutas Principales

### Públicas
- `/` - Página principal
- `/productos` - Catálogo de productos
- `/productos/<id>` - Detalle de producto
- `/categorias` - Lista de categorías
- `/auth/login` - Inicio de sesión
- `/auth/registro` - Registro de usuario

### Autenticadas (Cliente)
- `/auth/perfil` - Perfil del usuario
- `/pedidos` - Mis pedidos
- `/pedidos/crear` - Crear nuevo pedido
- `/pedidos/<id>` - Detalle de pedido

### Vendedor/Admin
- `/categorias/crear` - Crear categoría
- `/categorias/<id>/editar` - Editar categoría
- `/productos/crear` - Crear producto
- `/productos/<id>/editar` - Editar producto
- `/pedidos/<id>/editar` - Editar pedido

### Solo Admin
- `/admin/` - Panel de administración Flask-Admin

## Documentación del Reto Adicional

### Subida y Optimización de Imágenes

**Archivo**: `app/productos/utils.py`

#### ¿Cómo funciona?

1. **Validación**: Se verifica extensión y tamaño del archivo
2. **Seguridad**: Nombres únicos con UUID para evitar sobrescritura
3. **Almacenamiento**: Guardado en `app/static/uploads/productos/`
4. **Optimización**: Pillow redimensiona y comprime la imagen
5. **Limpieza**: Al actualizar/eliminar, se borra la imagen anterior

#### ¿Qué aprendimos?

- **Manejo de archivos** con Flask (FileStorage)
- **Validación de archivos** (extensión, tamaño)
- **Procesamiento de imágenes** con Pillow/PIL
- **Optimización automática** (resize, compress)
- **Gestión de almacenamiento** (crear carpetas, eliminar archivos)
- **Seguridad** (nombres únicos, validaciones)
- **Experiencia de usuario** (preview, actualización)

#### Código clave

```python
# Guardar y optimizar imagen
imagen_path = guardar_imagen(archivo, carpeta='productos')

# La función internamente:
# 1. Valida extensión y tamaño
# 2. Genera nombre único (UUID)
# 3. Guarda archivo
# 4. Optimiza con Pillow (resize + compress)
# 5. Retorna ruta relativa
```

## Contribuir

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'feat: agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Convenciones de Commits

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Formato, punto y coma faltante, etc.
- `refactor:` Refactorización de código
- `test:` Agregar tests
- `chore:` Tareas de mantenimiento

## Licencia

Este proyecto fue desarrollado como examen de Python con fines educativos.

## Contacto

- **Equipo**: [Nombres de los integrantes]
- **Repositorio**: [URL del repositorio]
- **Fecha**: Marzo 2026