import tornado.ioloop
import tornado.web
import os
import signal
from backend.db.connection import init_db, db
from backend.views.handlers import ComisionHandler

def make_app():
    return tornado.web.Application([
        (r"/api/comisiones", ComisionHandler),
    ],
    debug=True
    )

if __name__ == "__main__":
    init_db()

    app = make_app()
    port = int(os.environ.get("PORT", 8888))
    app.listen(port)
    print(f"Servidor Tornado escuchando en http://localhost:{port}")

    def shutdown_hook():
        print("Cerrando la base de datos y deteniendo el servidor.")
        try:
            if not db.is_closed():
                db.close()
        except Exception as e:
            print(f"Error al intentar cerrar la base de datos: {e}")
        finally:
            tornado.ioloop.IOLoop.current().stop()

    signal.signal(signal.SIGINT,
                  lambda sig, frame: tornado.ioloop.IOLoop.current().add_callback_from_signal(shutdown_hook))
    signal.signal(signal.SIGTERM,
                  lambda sig, frame: tornado.ioloop.IOLoop.current().add_callback_from_signal(shutdown_hook))

    tornado.ioloop.IOLoop.current().start()