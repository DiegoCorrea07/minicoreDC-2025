from backend.services.comision_service import ComisionService

class ComisionController:
    def __init__(self):
        self.comision_service = ComisionService()

    def obtener_comisiones(self, fecha_inicio: str, fecha_fin: str) -> dict:
        """
        Orquesta la obtención y cálculo de comisiones a través del servicio.
        """
        return self.comision_service.calcular_comisiones_en_rango(fecha_inicio, fecha_fin)