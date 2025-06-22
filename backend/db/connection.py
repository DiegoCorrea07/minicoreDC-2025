import sqlite3
import os

# Define la ruta de la base de datos para que esté dentro de una carpeta 'data' en backend
DATABASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
if not os.path.exists(DATABASE_DIR):
    os.makedirs(DATABASE_DIR) # Crea la carpeta 'data' si no existe

DATABASE = os.path.join(DATABASE_DIR, 'ventas.db')

def get_db_connection():
    """Establece y retorna una conexión a la base de datos."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conn

def init_db():
    """
    Inicializa la base de datos: crea tablas e inserta datos de ejemplo
    si no existen.
    """
    print(f"Inicializando base de datos en: {DATABASE}")
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Crear tabla Vendedor
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Vendedor (
                id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
            )
        ''')

        # Crear tabla Venta
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Venta (
                id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
                id_vendedor INTEGER,
                fecha_venta TEXT NOT NULL, -- Formato YYYY-MM-DD
                monto_venta REAL NOT NULL,
                FOREIGN KEY (id_vendedor) REFERENCES Vendedor(id_vendedor)
            )
        ''')

        # Crear tabla Regla
        # NOTA: Los nombres de las columnas en la DB son 'monto_minimo_para_comision' y 'porcentaje_comision'
        # para mapear 'Amount' y 'rule' respectivamente de tu imagen.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Regla (
                id_regla INTEGER PRIMARY KEY AUTOINCREMENT,
                porcentaje_comision REAL NOT NULL,
                monto_minimo_para_comision REAL NOT NULL
            )
        ''')
        conn.commit()

        # Insertar datos de ejemplo si las tablas están vacías
        # Vendedores
        if not cursor.execute("SELECT 1 FROM Vendedor").fetchone():
            print("Insertando vendedores de ejemplo...")
            cursor.execute("INSERT INTO Vendedor (nombre) VALUES ('Pedro')")
            cursor.execute("INSERT INTO Vendedor (nombre) VALUES ('Maria')")
            cursor.execute("INSERT INTO Vendedor (nombre) VALUES ('Juan')")
            conn.commit()

        # Reglas - ACTUALIZADO CON LOS DATOS DE LA IMAGEN
        if not cursor.execute("SELECT 1 FROM Regla").fetchone():
            print("Insertando reglas de ejemplo...")
            cursor.execute("INSERT INTO Regla (porcentaje_comision, monto_minimo_para_comision) VALUES (0.06, 600.0)")
            cursor.execute("INSERT INTO Regla (porcentaje_comision, monto_minimo_para_comision) VALUES (0.08, 500.0)")
            cursor.execute("INSERT INTO Regla (porcentaje_comision, monto_minimo_para_comision) VALUES (0.1, 800.0)")
            cursor.execute("INSERT INTO Regla (porcentaje_comision, monto_minimo_para_comision) VALUES (1.15, 1000.0)") # Nota: 1.15 es 115%, si fuera 15% debería ser 0.15
            conn.commit()
            print("Reglas de ejemplo insertadas.")

        # Ventas
        if not cursor.execute("SELECT 1 FROM Venta").fetchone():
            print("Insertando ventas de ejemplo...")
            # Ventas para Pedro (ID 1)
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (1, '2025-06-01', 50.0)")
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (1, '2025-06-05', 30.0)") # Total 80
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (1, '2025-06-10', 500.0)") # Total con las dos anteriores: 580

            # Ventas para Maria (ID 2)
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (2, '2025-05-29', 100.0)") # Fuera del rango de junio
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (2, '2025-06-15', 70.0)") # Total 70, no comisiona
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (2, '2025-06-20', 750.0)") # Total 820

            # Ventas para Juan (ID 3)
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (3, '2025-06-03', 90.0)")
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (3, '2025-06-07', 5.0)") # Total 95
            cursor.execute("INSERT INTO Venta (id_vendedor, fecha_venta, monto_venta) VALUES (3, '2025-06-25', 950.0)") # Total 1045
            conn.commit()
            print("Datos de ejemplo insertados.")
        else:
            print("Datos de ejemplo ya existen. Saltando inserción.")