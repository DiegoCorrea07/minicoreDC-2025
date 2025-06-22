from backend.db.connection import get_db_connection
from backend.models.regla import Regla

class ReglaRepository:
    def get_all_reglas(self) -> list[Regla]:
        """
        Obtiene todas las reglas de comisión, ordenadas por monto mínimo de forma ascendente.
        Esto facilita la lógica de selección en el servicio.
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            # Ordenar por monto_minimo_para_comision para facilitar la selección de reglas
            cursor.execute("SELECT id_regla, porcentaje_comision, monto_minimo_para_comision FROM Regla ORDER BY monto_minimo_para_comision ASC")
            reglas_data = cursor.fetchall()
            return [
                Regla(
                    row['id_regla'],
                    row['monto_minimo_para_comision'], # 'Amount' de la imagen
                    row['porcentaje_comision']         # 'rule' de la imagen
                )
                for row in reglas_data
            ]