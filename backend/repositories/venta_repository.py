from backend.db.connection import get_db_connection
from backend.models.venta import Venta

class VentaRepository:
    def get_ventas_by_date_range(self, fecha_inicio: str, fecha_fin: str) -> list[dict]:
        """
        Obtiene ventas y el nombre del vendedor dentro de un rango de fechas.
        Retorna una lista de diccionarios (cada dict es una fila de resultado).
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            query = """
                SELECT
                    V.nombre AS nombre_vendedor,
                    VT.monto_venta,
                    VT.fecha_venta,
                    VT.id_vendedor
                FROM
                    Venta AS VT
                JOIN
                    Vendedor AS V ON VT.id_vendedor = V.id_vendedor
                WHERE
                    VT.fecha_venta BETWEEN ? AND ?
                ORDER BY V.nombre, VT.fecha_venta
            """
            ventas_raw = cursor.execute(query, (fecha_inicio, fecha_fin)).fetchall()
            # Convertir Row objetos a diccionarios para ser más manejables
            return [dict(row) for row in ventas_raw]

    def add_venta(self, venta: Venta):
        """Agrega una nueva venta a la base de datos."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (?, ?, ?)",
                (venta.id_vendedor, venta.fecha_venta, venta.monto_venta)
            )
            conn.commit()