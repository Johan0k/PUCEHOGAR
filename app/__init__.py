from flask import Flask

from .routes.visitor_routes import visitor_bp
from .routes.auth_routes import auth_bp
from .routes.tenant_routes import tenant_bp
from .routes.admin_routes import admin_bp


def create_app():
    app = Flask(__name__)

    # Clave simple por ahora (luego va a config.py)
    app.secret_key = "dev-secret-key"

    # Registro de blueprints
    app.register_blueprint(visitor_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(tenant_bp, url_prefix="/tenant")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app
