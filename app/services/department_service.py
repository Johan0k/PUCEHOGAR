<<<<<<< HEAD
from typing import List, Optional
from ..domain.entities import Department
from ..repositories.interfaces import DepartmentRepository

class DepartmentService:
    def __init__(self, repo: DepartmentRepository):
        self.repo = repo

    def list_public(self) -> List[Department]:
        # Regla de negocio: solo públicos/disponibles (ya filtrado en repo)
        return self.repo.list_public()

    def get_detail(self, department_id: str) -> Optional[Department]:
        return self.repo.get_by_id(department_id)
=======
>>>>>>> parent of 5d29c1f (Project Updated)
