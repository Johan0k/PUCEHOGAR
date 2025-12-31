<<<<<<< HEAD

class Config:
    SECRET_KEY = "dev-secret-key"

    
    SUPABASE_URL = "https://ukujhsrxjppmmzhgdfnz.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVrdWpoc3J4anBwbW16aGdkZm56Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjcxMzUxMTAsImV4cCI6MjA4MjcxMTExMH0.l2XnQOX8F01PG4EE9XSXBYq7MGFBwxvm2FKPW64DxhY"


def get_config():
    """
    Intenta cargar config_local.py si existe.
    Si no existe, usa Config por defecto.
    """
    try:
        from .config import LocalConfig
        return LocalConfig
    except ImportError:
        return Config
=======
>>>>>>> parent of 5d29c1f (Project Updated)
