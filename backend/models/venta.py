from datetime import datetime

class Venta:
    def __init__(self, id_venta: int, id_vendedor: int, fecha_venta: str, monto_venta: float):
        if not isinstance(id_venta, int) or id_venta <= 0:
            raise ValueError("id_venta debe ser un entero positivo.")
        if not isinstance(id_vendedor, int) or id_vendedor <= 0:
            raise ValueError("id_vendedor debe ser un entero positivo.")
        try:
            datetime.strptime(fecha_venta, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Formato de fecha_venta inválido. Use 'YYYY-MM-DD'.")
        if not isinstance(monto_venta, (int, float)) or monto_venta <= 0:
            raise ValueError("monto_venta debe ser un número positivo.")

        self.id_venta = id_venta
        self.id_vendedor = id_vendedor
        self.fecha_venta = fecha_venta
        self.monto_venta = monto_venta

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "id_vendedor": self.id_vendedor,
            "fecha_venta": self.fecha_venta,
            "monto_venta": self.monto_venta
        }