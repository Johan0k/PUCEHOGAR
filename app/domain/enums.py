from enum import Enum

class DepartmentStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    RENTED = "RENTED"
    SOLD = "SOLD"

class DepartmentType(str, Enum):
    RENT = "RENT"
    SALE = "SALE"
