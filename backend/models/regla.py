from peewee import Model, AutoField, FloatField
from backend.db.connection import db

class Regla(Model):
    id_regla = AutoField()
    porcentaje_comision = FloatField()
    monto_minimo_para_comision = FloatField()

    class Meta:
        database = db
        table_name = 'Regla'
