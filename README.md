# 📋 Sistema de Gestión de Clientes

Sistema Python funcional para gestionar clientes y productos con persistencia en JSON.

## 🗂️ Estructura del Proyecto

```
proyecto/
├── src/
│   ├── validate.py      # Validaciones de campos
│   ├── service.py       # Lógica + persistencia
│   ├── file.py          # Manejo de archivos JSON
│   ├── integration.py   # Exportación de datos con pandas
│   └── main.py          # Programa principal
├── data/
│   └── records.json     # Archivo de datos (creado automáticamente)
└── README.md            # Este archivo
```

## 📦 Módulos

### validate.py

Funciones de validación para campos:

- `validate_id()`: Valida IDs positivos
- `validate_name()`: Mínimo 2 caracteres
- `validate_email()`: Formato válido
- `validate_product_name()`: No vacío
- `validate_quantity()`: Número positivo
- `validate_price()`: Número no negativo

### file.py

Manejo seguro de archivos JSON:

- `load_data()`: Carga datos, crea archivo si no existe
- `save_data()`: Guarda datos de forma segura
- Manejo de errores: JSON corrupto, permisos, etc.

### service.py

Clase `ClientService` que gestiona:

- Clientes con id, nombre, email, productos
- Prevención de duplicados (IDs y emails)
- Validaciones de todos los campos
- Persistencia automática en JSON
- Estadísticas (total clientes, productos, ingresos)

### main.py

Programa principal interactivo que:

- Inicia el menú de gestión de clientes
- Permite crear, listar, buscar, editar y eliminar registros
- Incluye exportación a CSV con pandas
- Muestra estadísticas del sistema

## ✅ Características

- ✅ Listas y diccionarios para estructura de datos
- ✅ Sets para prevenir duplicados (IDs, emails)
- ✅ Validaciones completas de campos
- ✅ Manejo seguro de archivos con try-except
- ✅ Persistencia real entre ejecuciones
- ✅ Crea directorio automáticamente
- ✅ Error handling para JSON corrupto

## 🚀 Uso

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python src/main.py
```

## 📌 Nueva característica

- Opción del menú: `7. Exportar registros a CSV`
- Genera un archivo en `data/clientes_reporte.csv` por defecto
- Usa `pandas` para convertir los registros en un `DataFrame` y ordenar los datos

## 📊 Estructura de Datos

### Cliente

```json
{
  "id": 1,
  "nombre": "Juan Pérez",
  "email": "juan@email.com",
  "productos": [
    {
      "nombre": "Laptop",
      "cantidad": 1,
      "precio": 1200.0
    }
  ]
}
```

## 💾 Persistencia

- Datos se guardan automáticamente en `data/records.json`
- Se crea vacío si no existe
- Se carga automáticamente al iniciar
- Manejo de errores si archivo está dañado
