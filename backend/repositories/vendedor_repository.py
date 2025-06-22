from backend.db.connection import get_db_connection
from backend.models.vendedor import Vendedor

class VendedorRepository:
    def get_vendedor_by_id(self, id_vendedor: int) -> Vendedor | None:
        """Obtiene un vendedor por su ID."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_vendedor, nombre FROM Vendedor WHERE id_vendedor = ?", (id_vendedor,))
            row = cursor.fetchone()
            if row:
                return Vendedor(row['id_vendedor'], row['nombre'])
            return None