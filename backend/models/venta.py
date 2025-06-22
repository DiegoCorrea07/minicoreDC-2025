from peewee import Model, AutoField, ForeignKeyField, DateField, FloatField
from backend.db.connection import db
from backend.models.vendedor import Vendedor

class Venta(Model):
    id_venta = AutoField()
    id_vendedor = ForeignKeyField(Vendedor, backref='ventas')
    fecha_venta = DateField(formats='%Y-%m-%d')
    monto_venta = FloatField()

    class Meta:
        database = db
        table_name = 'Venta'
