from dataclasses import dataclass
from .enums import DepartmentStatus, DepartmentType

@dataclass
class Department:
    id: str
    title: str
    address: str
    rooms: int
    price: float
    type: DepartmentType
    status: DepartmentStatus
    description: str | None
