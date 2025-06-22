from backend.db.connection import db
from backend.models.venta import Venta
from backend.models.vendedor import Vendedor
import datetime


class VentaRepository:
    def get_ventas_by_date_range(self, fecha_inicio: str, fecha_fin: str) -> list[dict]:
        ventas_data = []
        try:
            db.connect(reuse_if_open=True)

            start_date = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').date()

            query = Venta.select(
                Venta.id_vendedor,
                Vendedor.nombre.alias('nombre_vendedor'),
                Venta.monto_venta,
                Venta.fecha_venta
            ).join(Vendedor).where(
                (Venta.fecha_venta >= start_date) &
                (Venta.fecha_venta <= end_date)
            ).order_by(Vendedor.nombre, Venta.fecha_venta)

            for venta_item in query.dicts():
                ventas_data.append({
                    'id_vendedor': venta_item['id_vendedor'],
                    'nombre_vendedor': venta_item['nombre_vendedor'],
                    'monto_venta': venta_item['monto_venta'],
                    'fecha_venta': venta_item['fecha_venta']
                })
        except Exception as e:
            print(f"Error en VentaRepository.get_ventas_by_date_range: {e}")
            raise
        finally:
            if not db.is_closed():
                db.close()
        return ventas_data

    def add_venta(self, venta_data: dict) -> Venta:
        try:
            db.connect(reuse_if_open=True)

            fecha_obj = datetime.datetime.strptime(venta_data['fecha_venta'], '%Y-%m-%d').date()

            vendedor_instance = Vendedor.get_by_id(venta_data['id_vendedor'])

            venta = Venta.create(
                id_vendedor=vendedor_instance,
                fecha_venta=fecha_obj,
                monto_venta=venta_data['monto_venta']
            )
            return venta
        except Exception as e:
            print(f"Error en VentaRepository.add_venta: {e}")
            raise
        finally:
            if not db.is_closed():
                db.close()