<<<<<<< HEAD
from typing import Protocol, List, Optional
from ..domain.entities import Department

class DepartmentRepository(Protocol):
    def list_public(self) -> List[Department]: ...
    def get_by_id(self, department_id: str) -> Optional[Department]: ...
=======
>>>>>>> parent of 5d29c1f (Project Updated)
