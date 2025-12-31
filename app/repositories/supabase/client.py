<<<<<<< HEAD
from supabase import create_client, Client

class SupabaseClient:
    def __init__(self, url: str, key: str):
        print("SUPABASE_URL:", url)  # TEMPORAL
        self._client: Client = create_client(url, key)

    @property
    def client(self) -> Client:
        return self._client
=======
>>>>>>> parent of 5d29c1f (Project Updated)
