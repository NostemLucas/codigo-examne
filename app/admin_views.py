"""Vistas personalizadas de Flask-Admin con control de acceso por roles"""

from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for, flash


class SecureModelView(ModelView):
    """Vista de Flask-Admin con restricción de acceso solo para administradores"""

    def is_accessible(self):
        """Solo permite acceso a usuarios administradores autenticados"""
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        """Redirigir a login si no tiene acceso"""
        flash('Necesitas permisos de administrador para acceder a esta sección.', 'danger')
        return redirect(url_for('auth.login'))
