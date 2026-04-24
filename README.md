# 📋 Sistema de Gestión de Clientes

Sistema Python funcional para gestionar clientes y productos con persistencia en JSON.

## 🗂️ Estructura del Proyecto

```
proyecto/
├── src/
│   ├── validate.py      # Validaciones de campos
│   ├── service.py       # Lógica + persistencia
│   ├── file.py          # Manejo de archivos JSON
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

Programa de demostración que:

- Crea 3 clientes
- Intenta agregar duplicados (falla correctamente)
- Agrega productos
- Lista todos los registros
- Muestra estadísticas

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
# Ejecutar la demostración
python src/main.py
```

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
