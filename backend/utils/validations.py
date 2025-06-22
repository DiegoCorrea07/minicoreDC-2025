from datetime import datetime

class Validations:
    @staticmethod
    def is_valid_date_format(date_str: str, date_format: str = '%Y-%m-%d') -> bool:
        """Verifica si una cadena de texto tiene el formato de fecha especificado."""
        try:
            datetime.strptime(date_str, date_format)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_number(value, min_val=None, max_val=None) -> bool:
        """Verifica si un valor es un número y está dentro de un rango opcional."""
        if not isinstance(value, (int, float)):
            return False
        if min_val is not None and value < min_val:
            return False
        if max_val is not None and value > max_val:
            return False
        return True