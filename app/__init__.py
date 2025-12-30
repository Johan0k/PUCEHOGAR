from flask import Flask
from .config import get_config
from .deps import build_container

from .routes.visitor_routes import visitor_bp
from .routes.auth_routes import auth_bp
from .routes.tenant_routes import tenant_bp
from .routes.admin_routes import admin_bp

def create_app():
    app = Flask(__name__)
    cfg = get_config()
    app.secret_key = cfg.SECRET_KEY

    app.config["SUPABASE_URL"] = cfg.SUPABASE_URL
    app.config["SUPABASE_KEY"] = cfg.SUPABASE_KEY

    app.extensions["container"] = build_container(cfg)

    app.register_blueprint(visitor_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(tenant_bp, url_prefix="/tenant")
    app.register_blueprint(admin_bp, url_prefix="/admin")

    return app
