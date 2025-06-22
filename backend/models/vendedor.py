class Vendedor:
    def __init__(self, id_vendedor: int, nombre: str):
        if not isinstance(id_vendedor, int) or id_vendedor <= 0:
            raise ValueError("id_vendedor debe ser un entero positivo.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del vendedor no puede estar vacío.")
        self.id_vendedor = id_vendedor
        self.nombre = nombre

    def to_dict(self):
        return {
            "id_vendedor": self.id_vendedor,
            "nombre": self.nombre
        }