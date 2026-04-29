# MÓDULO 4 — Menú Interactivo en Consola (UI)

## Descripción

Este módulo implementa un menú interactivo en consola utilizando **colorama** para proporcionar una interfaz amigable y colorida al usuario. El menú está completamente conectado al CRUD de gestión de clientes.

## Archivos

### `menu.py`

Contiene la clase `MenuInteractivo` con:

- **Título y presentación** con colores ANSI
- **Menú principal** con 6 opciones principales + salir
- **Validación de entradas** con manejo de excepciones para letras vs números
- **Métodos para cada operación CRUD**:
  - Crear nuevo registro
  - Listar registros
  - Buscar por ID
  - Editar (nombre y/o email)
  - Eliminar con confirmación
  - Ver estadísticas

### `main.py` (Actualizado)

Ahora llama al menú interactivo en lugar de ejecutar una demostración estática.

### `demo.py` (Opcional)

Script de demostración que pre-carga registros de prueba antes de mostrar el menú.

## Características Implementadas

### ✅ Requisitos Cumplidos

1. **Menú interactivo**
   - Ciclo infinito hasta que se selecciona "Salir"
   - Presentación clara con colores y emojis
   - Opciones numeradas (0-6)

2. **Validación de entradas**
   - Manejo de `try-except` para convertir strings a números
   - Verificación de opciones válidas (0-6)
   - Confirmación para operaciones destructivas (eliminar)

3. **Flujo CRUD completo**
   - ✅ **Crear**: Formulario para ingresar ID, nombre y email
   - ✅ **Guardar**: Automático en cada operación
   - ✅ **Listar**: Muestra todos los registros ordenados
   - ✅ **Editar**: Permite cambiar nombre y/o email
   - ✅ **Eliminar**: Con confirmación de usuario

4. **Colores y formato**
   - Usando `colorama` para compatibilidad multiplataforma
   - Colores por tipo de elemento:
     - 🟦 CYAN: Títulos y separadores
     - 🟩 GREEN: Números de opción
     - 🟨 YELLOW: Títulos de sección
     - 🔴 RED: Errores y advertencias
     - 🟣 MAGENTA: Prompts de entrada

## Uso

### Ejecutar el menú interactivo

```bash
cd src
python main.py
```

### Ejecutar la demostración con datos de prueba

```bash
python demo.py
```

### Importar en otro módulo

```python
from service import ClientService
from menu import MenuInteractivo

service = ClientService('data/records.json')
menu = MenuInteractivo(service)
menu.ejecutar()
```

## Flujo de Usuario

```
1. El programa inicia el menú
2. Usuario ve opciones numeradas (1-6) más opción 0 para salir
3. Usuario ingresa número
   - Si es letra → "❌ Error: Ingrese un número válido"
   - Si es inválido → "❌ Opción no válida"
   - Si es válido → Ejecuta la opción
4. Después de cada operación → "Presione Enter para continuar..."
5. Vuelve al menú
6. Al seleccionar 0 → "Salir" y termina el programa
```

## Manejo de Errores

| Entrada del Usuario         | Comportamiento                              |
| --------------------------- | ------------------------------------------- |
| Letra en campo numérico     | Reintenta el ingreso con mensaje de error   |
| Opción fuera de rango (0-6) | Muestra "Opción no válida" y vuelve al menú |
| Cliente no existe           | "❌ Registro con ID X no existe"            |
| ID duplicado                | "❌ Error: ID X ya existe"                  |
| Email duplicado             | "❌ Error: Email Y ya está registrado"      |
| Ctrl+C durante operación    | "⚠️ Operación cancelada"                    |

## Estadísticas

El menú incluye una opción para ver:

- Cantidad de clientes registrados
- Cantidad total de productos
- Ingresos totales (suma de cantidad × precio de todos los productos)

## Ejemplo de Interacción

```
============================================================
🎯 SISTEMA DE GESTIÓN DE CLIENTES
============================================================

📋 MENÚ PRINCIPAL
1. ➕ Crear nuevo registro
2. 📋 Listar todos los registros
3. 🔍 Buscar registro por ID
4. ✏️  Editar registro
5. 🗑️  Eliminar registro
6. 📊 Ver estadísticas
0. 🚪 Salir
------------------------------------------------------------
Ingrese su opción: 1

➕ CREAR NUEVO REGISTRO
ID del cliente: 1
Nombre del cliente: Juan Pérez
Email del cliente: juan@email.com
✅ Registro creado exitosamente
Datos guardados automáticamente en: data/records.json
```

## Dependencias

- `colorama` - Para colores en consola multiplataforma
- `service.py` - Servicio CRUD de gestión de clientes
- `validate.py` - Validaciones de campos

## Criterios de Aceptación ✅

- ✅ El menú se repite hasta seleccionar "Salir"
- ✅ No se rompe si el usuario escribe letras en lugar de números
- ✅ Flujo completo: crear → guardar → listar → editar → eliminar
- ✅ Interfaz visual con colores y emojis
- ✅ Validación de todas las entradas
- ✅ Confirmación para operaciones destructivas
