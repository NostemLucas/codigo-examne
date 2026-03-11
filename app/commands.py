"""Comandos CLI personalizados para la aplicación"""

import click
from flask.cli import with_appcontext
from app.extensions import db
from app.models import Usuario, Categoria


@click.command('init-db')
@with_appcontext
def init_db():
    """Inicializar la base de datos con datos de prueba"""
    click.echo('Creando tablas de base de datos...')
    db.create_all()

    # Crear categorías iniciales si no existen
    categorias = [
        {'nombre': 'Rosas', 'descripcion': 'Rosas de diferentes colores y variedades', 'slug': 'rosas'},
        {'nombre': 'Orquídeas', 'descripcion': 'Orquídeas exóticas y elegantes', 'slug': 'orquideas'},
        {'nombre': 'Plantas de Interior', 'descripcion': 'Plantas perfectas para decorar tu hogar', 'slug': 'plantas-interior'},
        {'nombre': 'Arreglos Florales', 'descripcion': 'Arreglos personalizados para toda ocasión', 'slug': 'arreglos-florales'},
        {'nombre': 'Plantas Suculentas', 'descripcion': 'Suculentas fáciles de cuidar', 'slug': 'suculentas'},
    ]

    for cat_data in categorias:
        if not Categoria.query.filter_by(slug=cat_data['slug']).first():
            categoria = Categoria(**cat_data)
            db.session.add(categoria)
            click.echo(f'  - Categoría creada: {cat_data["nombre"]}')

    db.session.commit()
    click.echo('Base de datos inicializada correctamente!')


@click.command('create-admin')
@click.option('--username', prompt='Username', help='Nombre de usuario')
@click.option('--email', prompt='Email', help='Email del administrador')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Contraseña')
@click.option('--nombre', prompt='Nombre completo', help='Nombre completo')
@with_appcontext
def create_admin(username, email, password, nombre):
    """Crear un usuario administrador"""
    # Verificar si ya existe
    if Usuario.query.filter_by(username=username).first():
        click.echo(f'Error: El usuario {username} ya existe.')
        return

    if Usuario.query.filter_by(email=email).first():
        click.echo(f'Error: El email {email} ya está registrado.')
        return

    # Crear administrador
    admin = Usuario(
        username=username,
        email=email,
        nombre_completo=nombre,
        rol='admin',
        activo=True
    )
    admin.set_password(password)

    db.session.add(admin)
    db.session.commit()

    click.echo(f'Administrador {username} creado exitosamente!')
