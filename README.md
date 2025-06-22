# Sistema de Cálculo de Comisiones de Ventas
Sistema backend para el cálculo automatizado de comisiones de vendedores basado en reglas configurables. Desarrollado con **Python (Tornado)** y **SQLite**, implementa arquitectura MVC con patrones de repositorio y servicios.

---

## Descripción General
Este sistema permite calcular comisiones de vendedores aplicando reglas dinámicas basadas en el total de ventas en un rango de fechas específico. Incluye:
- **Cálculo automatizado de comisiones**: basado en reglas configurables por montos mínimos.
- **API REST**: endpoint para consultar comisiones por rango de fechas.
- **Arquitectura MVC**: separación clara de responsabilidades con controladores, servicios y repositorios.
- **Base de datos SQLite**: con modelos Peewee ORM para fácil gestión.
- **Validaciones backend**: formato de fechas y parámetros de entrada.
- **CORS habilitado**: para integración con frontends web.

---

## Instalación

### Requisitos
- Python 3.13+
- Dependencias: tornado, peewee

### Setup del Backend
1. Clona el repositorio:
```bash
git clone https://github.com/DiegoCorrea07/minicoreDC-2025.git
cd minicoreDC-2025
```

2. Crea un entorno virtual:
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r backend/requirements.txt
```

4. Inicia el servidor:
```bash
python backend/app.py
```

Servidor disponible en: **http://localhost:8888**

---

## Reglas de Comisión

El sistema incluye las siguientes reglas predefinidas:

| Monto Mínimo | Porcentaje de Comisión |
|--------------|----------------------|
| $500.00      | 6%                  |
| $600.00      | 8%                  |
| $800.00      | 10%                 |
| $1,000.00    | 15%                 |

**Lógica de aplicación**: Se aplica la regla con el monto mínimo más alto que sea menor o igual al total de ventas del vendedor.

---

## Datos de Prueba

### Vendedores
- Pedro Cadenas
- Maria Jimenez  
- Juan Castro
- Luis Perez

### Ventas de Ejemplo (Junio 2025)
```
Pedro Cadenas: $50 + $30 + $500 = $580 → Comisión: 6% = $34.80
Maria Jimenez: $100 + $70 + $750 = $920 → Comisión: 10% = $92.00
Juan Castro: $90 + $5 + $950 = $1,045 → Comisión: 15% = $156.75
Luis Perez: $300 + $270 = $570 → Comisión: 6% = $34.20
```

---

## API Endpoints

### Cálculo de Comisiones
**GET** `/api/comisiones`

#### Parámetros Query
- `fecha_inicio` (requerido): Fecha inicio en formato `YYYY-MM-DD`
- `fecha_fin` (requerido): Fecha fin en formato `YYYY-MM-DD`

#### Ejemplo de Petición
```bash
curl "http://localhost:8888/api/comisiones?fecha_inicio=2025-06-01&fecha_fin=2025-06-30"
```

#### Ejemplo de Respuesta
```json
{
  "Pedro Cadenas": {
    "total_ventas": 580.0,
    "comision": 34.8
  },
  "Maria Jimenez": {
    "total_ventas": 920.0,
    "comision": 92.0
  },
  "Juan Castro": {
    "total_ventas": 1045.0,
    "comision": 156.75
  },
  "Luis Perez": {
    "total_ventas": 570.0,
    "comision": 34.2
  }
}
```

#### Códigos de Respuesta
- `200`: Éxito
- `400`: Error en parámetros (fechas faltantes o formato inválido)
- `500`: Error interno del servidor

---

## Características Técnicas

### Arquitectura
- **Patrón MVC**: Separación clara entre modelos, vistas y controladores
- **Patrón Repositorio**: Abstracción de acceso a datos
- **Patrón Servicio**: Lógica de negocio encapsulada
- **ORM Peewee**: Mapeo objeto-relacional para SQLite

### Funcionalidades
- Cálculo automático de comisiones por rango de fechas
- Aplicación de reglas dinámicas de comisión
- Agrupación y sumarización de ventas por vendedor
- Validaciones de entrada (formato de fechas)
- Manejo de errores y logging
- CORS habilitado para integración frontend
- Inicialización automática de datos de prueba

### Validaciones
- Formato de fecha `YYYY-MM-DD`
- Parámetros requeridos (fecha_inicio, fecha_fin)
- Manejo seguro de conexiones a base de datos

---

## Configuración de Base de Datos

La base de datos se inicializa automáticamente al ejecutar la aplicación por primera vez:

1. **Creación de tablas**: Vendedor, Venta, Regla
2. **Datos iniciales**: Vendedores, reglas de comisión y ventas de ejemplo
3. **Ubicación**: `backend/data/ventas.db`

### Modelos de Datos

#### Vendedor
```python
id_vendedor: AutoField (PK)
nombre: CharField
```

#### Venta
```python
id_venta: AutoField (PK)
id_vendedor: ForeignKey → Vendedor
fecha_venta: DateField
monto_venta: FloatField
```

#### Regla
```python
id_regla: AutoField (PK)
porcentaje_comision: FloatField
monto_minimo_para_comision: FloatField
```

---

## Repositorios

### Back-end
```
https://github.com/DiegoCorrea07/minicoreDC-2025.git
```

### Front-end
```
https://github.com/DiegoCorrea07/frontend-minicore-2025.git
```
---

## Enlace de página desplegada en render
```
https://frontend-minicore-2025.onrender.com
```

## Consideraciones de Producción

### Recomendaciones
- Usar PostgreSQL o MySQL en lugar de SQLite para producción
- Implementar autenticación y autorización
- Agregar logging estructurado
- Configurar variables de entorno para configuración
- Implementar tests unitarios y de integración
- Usar conexión pool para base de datos

### Variables de Entorno Sugeridas
```bash
DATABASE_URL=sqlite:///path/to/database.db
PORT=8888
DEBUG=False
LOG_LEVEL=INFO
```

---

## Contribución

1. Fork el repositorio
2. Crea una nueva rama: `git checkout -b feature/nueva-funcionalidad`
3. Haz commit: `git commit -m "Agrega nueva funcionalidad"`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

## Autor
- **Diego Correa**
- GitHub: [@DiegoCorrea07](https://github.com/DiegoCorrea07)

---

## Licencia
Este proyecto está bajo licencia **MIT**.

---
