"""App Factory para la aplicación Flask"""

from flask import Flask
from app.config import config
from app.extensions import db, migrate, login_manager, admin


def create_app(config_name='default'):
    """
    Factory para crear la aplicación Flask

    Args:
        config_name: Nombre de la configuración a usar (development, production, testing)

    Returns:
        app: Instancia de la aplicación Flask
    """
    app = Flask(__name__)

    # Cargar configuración
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)

    # Registrar blueprints (módulos)
    register_blueprints(app)

    # Configurar Flask-Admin
    configure_admin(app)

    # Registrar comandos CLI personalizados
    register_commands(app)

    # Registrar filtros de templates
    register_template_filters(app)

    return app


def register_blueprints(app):
    """Registrar todos los blueprints de la aplicación"""
    from app.auth import auth_bp
    from app.categorias import categorias_bp
    from app.productos import productos_bp
    from app.pedidos import pedidos_bp
    from app.tienda import tienda_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(categorias_bp, url_prefix='/categorias')
    app.register_blueprint(productos_bp, url_prefix='/productos')
    app.register_blueprint(pedidos_bp, url_prefix='/pedidos')
    app.register_blueprint(tienda_bp)  # Tienda en /tienda

    # Ruta principal
    from app.views import main_bp
    app.register_blueprint(main_bp)


def configure_admin(app):
    """Configurar Flask-Admin con vistas personalizadas"""
    from app.models import Usuario, Categoria, Producto, Pedido, DetallePedido
    from app.admin_views import SecureModelView

    with app.app_context():
        admin.add_view(SecureModelView(Usuario, db.session, name='Usuarios', category='Gestión'))
        admin.add_view(SecureModelView(Categoria, db.session, name='Categorías', category='Gestión'))
        admin.add_view(SecureModelView(Producto, db.session, name='Productos', category='Gestión'))
        admin.add_view(SecureModelView(Pedido, db.session, name='Pedidos', category='Ventas'))
        admin.add_view(SecureModelView(DetallePedido, db.session, name='Detalles', category='Ventas'))


def register_commands(app):
    """Registrar comandos CLI personalizados"""
    from app.commands import init_db, create_admin

    app.cli.add_command(init_db)
    app.cli.add_command(create_admin)


def register_template_filters(app):
    """Registrar filtros personalizados para templates"""
    @app.template_filter('currency')
    def currency_filter(value):
        """Formatear valor como moneda"""
        try:
            return f"${float(value):,.2f}"
        except (ValueError, TypeError):
            return "$0.00"

    @app.template_filter('datetime')
    def datetime_filter(value, format='%d/%m/%Y %H:%M'):
        """Formatear datetime"""
        if value is None:
            return ""
        return value.strftime(format)

    @app.template_filter('fix_image_path')
    def fix_image_path(value):
        """Arreglar rutas de imágenes para compatibilidad con formatos antiguos"""
        if not value:
            return None
        # Si ya tiene 'uploads/' al inicio, dejarla como está
        if value.startswith('uploads/'):
            return value
        # Si empieza con 'productos/' o similar, agregar 'uploads/' al inicio
        return f"uploads/{value}"


@login_manager.user_loader
def load_user(user_id):
    """Cargar usuario para Flask-Login"""
    from app.models import Usuario
    return Usuario.query.get(int(user_id))
