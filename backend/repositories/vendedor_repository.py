from backend.db.connection import db
from backend.models.vendedor import Vendedor

class VendedorRepository:
    def get_vendedor_by_id(self, id_vendedor: int) -> Vendedor | None:
        """Obtiene un vendedor por su ID usando Peewee."""
        try:
            db.connect(reuse_if_open=True)
            # Peewee's get_or_none para obtener una instancia o None si no existe
            vendedor = Vendedor.get_or_none(Vendedor.id_vendedor == id_vendedor)
            return vendedor
        except Exception as e:
            print(f"Error en VendedorRepository.get_vendedor_by_id: {e}")
            raise
        finally:
            if not db.is_closed():
                db.close()

    def get_vendedor_by_name(self, nombre: str) -> Vendedor | None:
        """Obtiene un vendedor por su nombre usando Peewee."""
        try:
            db.connect(reuse_if_open=True)
            vendedor = Vendedor.get_or_none(Vendedor.nombre == nombre)
            return vendedor
        except Exception as e:
            print(f"Error en VendedorRepository.get_vendedor_by_name: {e}")
            raise
        finally:
            if not db.is_closed():
                db.close()

    def get_all_vendedores(self) -> list[Vendedor]:
        """Obtiene todos los vendedores usando Peewee."""
        vendedores_list = []
        try:
            db.connect(reuse_if_open=True)
            for vendedor_peewee in Vendedor.select():
                vendedores_list.append(vendedor_peewee)
        except Exception as e:
            print(f"Error en VendedorRepository.get_all_vendedores: {e}")
            raise
        finally:
            if not db.is_closed():
                db.close()
        return vendedores_list