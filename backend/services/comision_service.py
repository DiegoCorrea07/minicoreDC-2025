from backend.repositories.venta_repository import VentaRepository
from backend.repositories.regla_repository import ReglaRepository
from backend.models.regla import Regla


class ComisionService:
    def __init__(self):
        self.venta_repo = VentaRepository()
        self.regla_repo = ReglaRepository()

    def _get_applicable_rule(self, total_ventas: float, reglas: list[Regla]) -> Regla | None:
        """
        Selecciona la regla de comisión más adecuada para un total de ventas.
        Busca la regla con el 'monto_minimo_para_comision' más alto que sea
        menor o igual al 'total_ventas'.
        """
        applicable_rule = None

        for regla in reglas:
            if total_ventas >= regla.monto_minimo_para_comision:
                applicable_rule = regla
            else:
                break
        return applicable_rule

    def calcular_comisiones_en_rango(self, fecha_inicio: str, fecha_fin: str) -> dict:
        """
        Calcula las comisiones de los vendedores para un rango de fechas dado.
        Aplica la regla de comisión correspondiente según el total de ventas del vendedor.
        Retorna un diccionario con los resultados por vendedor.
        """
        ventas = self.venta_repo.get_ventas_by_date_range(fecha_inicio, fecha_fin)
        all_reglas = self.regla_repo.get_all_reglas()

        if not all_reglas:
            print("Advertencia: No se han configurado reglas de comisión. Todas las comisiones serán 0.")

        comisiones_por_vendedor = {}

        # 1. Agrupar ventas por vendedor y sumar montos
        for venta in ventas:
            nombre_vendedor = venta['nombre_vendedor']
            monto_venta = venta['monto_venta']

            if nombre_vendedor not in comisiones_por_vendedor:
                comisiones_por_vendedor[nombre_vendedor] = {
                    "total_ventas": 0.0,
                    "comision": 0.0  # Inicializar comisión a 0
                }
            comisiones_por_vendedor[nombre_vendedor]["total_ventas"] += monto_venta

        # 2. Calcular comisiones aplicando la regla más adecuada
        for vendedor_nombre, datos in comisiones_por_vendedor.items():
            total_ventas_vendedor = datos["total_ventas"]

            regla_aplicable = self._get_applicable_rule(total_ventas_vendedor, all_reglas)

            if regla_aplicable:
                comision_calculada = total_ventas_vendedor * regla_aplicable.porcentaje_comision
                datos["comision"] = comision_calculada

            datos["total_ventas"] = round(datos["total_ventas"], 2)
            datos["comision"] = round(datos["comision"], 2)

        return comisiones_por_vendedor