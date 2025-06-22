from peewee import Model, AutoField, CharField
from backend.db.connection import db

class Vendedor(Model):
    id_vendedor = AutoField()
    nombre = CharField()

    class Meta:
        database = db
        table_name = 'Vendedor'
