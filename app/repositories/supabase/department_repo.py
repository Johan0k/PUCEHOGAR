from typing import List, Optional
from ..interfaces import DepartmentRepository
from ...domain.entities import Department
from ...domain.enums import DepartmentStatus, DepartmentType
from .client import SupabaseClient

class SupabaseDepartmentRepository(DepartmentRepository):
    def __init__(self, sb: SupabaseClient):
        self.sb = sb.client

    def list_public(self) -> List[Department]:
        res = self.sb.table("departments")\
            .select("id,title,address,rooms,price,type,status,description")\
            .eq("status", "AVAILABLE")\
            .order("created_at", desc=True)\
            .execute()

        data = res.data or []
        return [self._to_entity(row) for row in data]

    def get_by_id(self, department_id: str) -> Optional[Department]:
        res = self.sb.table("departments")\
            .select("id,title,address,rooms,price,type,status,description")\
            .eq("id", department_id)\
            .limit(1)\
            .execute()

        data = res.data or []
        if not data:
            return None
        return self._to_entity(data[0])

    def _to_entity(self, row: dict) -> Department:
        return Department(
            id=row["id"],
            title=row["title"],
            address=row["address"],
            rooms=int(row.get("rooms") or 0),
            price=float(row.get("price") or 0),
            type=DepartmentType(row["type"]),
            status=DepartmentStatus(row["status"]),
            description=row.get("description"),
        )
