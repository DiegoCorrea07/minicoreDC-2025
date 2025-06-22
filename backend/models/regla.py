class Regla:
    def __init__(self, id_regla: int, monto_minimo_para_comision: float, porcentaje_comision: float):
        if not isinstance(id_regla, int) or id_regla <= 0:
            raise ValueError("id_regla debe ser un entero positivo.")
        if not isinstance(monto_minimo_para_comision, (int, float)) or monto_minimo_para_comision < 0:
            raise ValueError("monto_minimo_para_comision debe ser un número no negativo.")
        if not isinstance(porcentaje_comision, (int, float)) or porcentaje_comision < 0:
            raise ValueError("porcentaje_comision debe ser un número no negativo.")

        self.id_regla = id_regla
        self.monto_minimo_para_comision = monto_minimo_para_comision
        self.porcentaje_comision = porcentaje_comision

    def to_dict(self):
        return {
            "id_regla": self.id_regla,
            "monto_minimo_para_comision": self.monto_minimo_para_comision,
            "porcentaje_comision": self.porcentaje_comision
        }