import os
from peewee import SqliteDatabase, Model, AutoField, FloatField, CharField, ForeignKeyField, DateField

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, '..', 'data')
os.makedirs(DB_DIR, exist_ok=True)

DATABASE_PATH = os.path.join(DB_DIR, 'ventas.db')

db = SqliteDatabase(DATABASE_PATH)

def init_db():
    from backend.models.vendedor import Vendedor
    from backend.models.venta import Venta
    from backend.models.regla import Regla
    import datetime

    db.connect()

    try:
        db.create_tables([Vendedor, Venta, Regla], safe=True)

        with db.atomic():
            if Vendedor.select().count() == 0:
                Vendedor.create(nombre='Pedro Cadenas')
                Vendedor.create(nombre='Maria Jimenez')
                Vendedor.create(nombre='Juan Castro')
                Vendedor.create(nombre='Luis Perez')

            if Regla.select().count() == 0:
                Regla.create(porcentaje_comision=0.06, monto_minimo_para_comision=500.0)
                Regla.create(porcentaje_comision=0.08, monto_minimo_para_comision=600.0)
                Regla.create(porcentaje_comision=0.1, monto_minimo_para_comision=800.0)
                Regla.create(porcentaje_comision=0.15, monto_minimo_para_comision=1000.0)

            if Venta.select().count() == 0:
                pedro = Vendedor.get(nombre='Pedro Cadenas')
                maria = Vendedor.get(nombre='Maria Jimenez')
                juan = Vendedor.get(nombre='Juan Castro')
                luis = Vendedor.get(nombre='Luis Perez')

                Venta.create(id_vendedor=pedro, fecha_venta=datetime.date(2025, 6, 1), monto_venta=50.0)
                Venta.create(id_vendedor=pedro, fecha_venta=datetime.date(2025, 6, 5), monto_venta=30.0)
                Venta.create(id_vendedor=pedro, fecha_venta=datetime.date(2025, 6, 10), monto_venta=500.0)

                Venta.create(id_vendedor=maria, fecha_venta=datetime.date(2025, 5, 29), monto_venta=100.0)
                Venta.create(id_vendedor=maria, fecha_venta=datetime.date(2025, 6, 15), monto_venta=70.0)
                Venta.create(id_vendedor=maria, fecha_venta=datetime.date(2025, 6, 20), monto_venta=750.0)

                Venta.create(id_vendedor=juan, fecha_venta=datetime.date(2025, 6, 3), monto_venta=90.0)
                Venta.create(id_vendedor=juan, fecha_venta=datetime.date(2025, 6, 7), monto_venta=5.0)
                Venta.create(id_vendedor=juan, fecha_venta=datetime.date(2025, 6, 25), monto_venta=950.0)

                Venta.create(id_vendedor=luis, fecha_venta=datetime.date(2025, 6, 15), monto_venta=300.0)
                Venta.create(id_vendedor=luis, fecha_venta=datetime.date(2025, 6, 20), monto_venta=270.0)
    finally:
        if not db.is_closed():
            db.close()