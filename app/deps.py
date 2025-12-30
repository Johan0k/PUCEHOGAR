from typing import Dict, Any
from .repositories.supabase.client import SupabaseClient
from .repositories.supabase.department_repo import SupabaseDepartmentRepository
from .services.department_service import DepartmentService

def build_container(config) -> Dict[str, Any]:
    sb = SupabaseClient(config.SUPABASE_URL, config.SUPABASE_KEY)
    department_repo = SupabaseDepartmentRepository(sb)
    department_service = DepartmentService(department_repo)

    return {
        "department_service": department_service,
    }
