import json
import tornado.web
import traceback
from backend.controllers.comision_controller import ComisionController
from backend.utils.validations import Validations

class CORSRequestHandler(tornado.web.RequestHandler):
    """
    Clase base para todos los handlers que implementa cabeceras CORS
    y un handler OPTIONS para preflight requests.
    """

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def options(self, *args, **kwargs):
        self.set_status(204)
        self.finish()


class ComisionHandler(CORSRequestHandler):
    """
    Handler para la API de cálculo de comisiones.
    Hereda de CORSRequestHandler para manejar las cabeceras CORS.
    """

    def initialize(self):
        # Aquí inicializamos el controlador
        self.comision_controller = ComisionController()

    async def get(self):
        try:

            fecha_inicio_str = self.get_argument("fecha_inicio", None)
            fecha_fin_str = self.get_argument("fecha_fin", None)

            if not fecha_inicio_str or not fecha_fin_str:
                self.set_status(400)
                self.write(json.dumps({"error": "Las fechas de inicio y fin son requeridas."}))
                return

            if not Validations.is_valid_date_format(fecha_inicio_str) or \
                    not Validations.is_valid_date_format(fecha_fin_str):
                self.set_status(400)
                self.write(json.dumps({"error": "Formato de fecha inválido. Use 'YYYY-MM-DD'."}))
                return

            # Llamar al controlador para calcular las comisiones
            resultados = self.comision_controller.obtener_comisiones(fecha_inicio_str, fecha_fin_str)

            self.set_header("Content-Type", "application/json")
            self.set_status(200)
            self.write(json.dumps(resultados))

        except ValueError as ve:
            # Errores de validación o lógica de negocio específica
            self.set_status(400)
            self.write(json.dumps({"error": str(ve)}))
        except Exception as e:
            # Captura cualquier otra excepción no manejada
            print(f"\n!!!! ERROR CAPTURADO EN COMISIONHANDLER.GET: {e} !!!!")
            traceback.print_exc()  # Imprime el stack trace para depuración
            self.set_status(500)
            self.write(json.dumps({
                                      "error": f"Error interno del servidor: {str(e)}. Verifique la consola del servidor para más detalles."}))
