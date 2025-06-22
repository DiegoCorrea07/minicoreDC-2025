from backend.db.connection import db
from backend.models.regla import Regla

class ReglaRepository:
    def get_all_reglas(self) -> list[Regla]:
        """
        Obtiene todas las reglas de comisión, ordenadas por monto mínimo de forma ascendente,
        usando Peewee.
        """
        reglas_list = []
        try:
            db.connect(reuse_if_open=True)

            for regla_peewee in Regla.select().order_by(Regla.monto_minimo_para_comision.asc()):
                reglas_list.append(regla_peewee)
        except Exception as e:
            print(f"Error en ReglaRepository.get_all_reglas: {e}")
            raise
        finally:
            if not db.is_closed():
                db.close()
        return reglas_list