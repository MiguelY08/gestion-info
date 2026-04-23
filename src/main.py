from service import ClienteService

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 60)
    print("SISTEMA DE GESTIÓN DE CLIENTES")
    print("=" * 60)
    print("1. Agregar cliente")
    print("2. Listar clientes")
    print("3. Ver detalles de cliente")
    print("4. Ver duplicados")
    print("5. Cargar datos de ejemplo")
    print("6. Salir")
    print("=" * 60)

def agregar_cliente_interactivo(servicio):
    """Permite agregar un cliente interactivamente"""
    try:
        print("\n--- Agregar Nuevo Cliente ---")
        id_cliente = int(input("ID del cliente: "))
        nombre = input("Nombre del cliente: ")
        email = input("Email del cliente: ")
        
        productos = []
        agregar_prod = input("¿Desea agregar productos? (s/n): ").lower()
        
        if agregar_prod == 's':
            while True:
                producto = {
                    'productName': input("Nombre del producto: "),
                    'quantity': int(input("Cantidad: ")),
                    'price': float(input("Precio unitario: "))
                }
                productos.append(producto)
                
                otro = input("¿Agregar otro producto? (s/n): ").lower()
                if otro != 's':
                    break
        
        cliente = servicio.agregar_cliente(id_cliente, nombre, email, productos)
        
        if cliente:
            print(f"\n[OK] Cliente agregado exitosamente: {cliente['name']} (ID: {cliente['id']})")
        else:
            print("\n[ERROR] No se pudo agregar el cliente. Verifique los datos.")
            
    except ValueError as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Error inesperado: {e}")

def listar_clientes_interactivo(servicio):
    """Muestra todos los clientes"""
    clientes = servicio.listar_clientes()
    
    if not clientes:
        print("\n[ERROR] No hay clientes registrados.")
        return
    
    print("\n" + "=" * 60)
    print("LISTADO DE CLIENTES")
    print("=" * 60)
    
    for cliente in clientes:
        print(f"\n[CLIENTE] {cliente['name']}")
        print(f"   ID: {cliente['id']}")
        print(f"   Email: {cliente['email']}")
        print(f"   Productos: {len(cliente['products'])}")
        total = servicio.obtener_total_cliente(cliente['id'])
        print(f"   Total gastado: ${total:.2f}")

def ver_detalles_cliente(servicio):
    """Muestra detalles de un cliente específico"""
    try:
        id_cliente = int(input("\nIngrese el ID del cliente: "))
        
        clientes = servicio.listar_clientes()
        cliente = None
        
        for c in clientes:
            if c['id'] == id_cliente:
                cliente = c
                break
        
        if not cliente:
            print("[ERROR] Cliente no encontrado.")
            return
        
        print("\n" + "=" * 60)
        print(f"DETALLES DEL CLIENTE: {cliente['name']}")
        print("=" * 60)
        print(f"ID: {cliente['id']}")
        print(f"Email: {cliente['email']}")
        print(f"\nProductos:")
        
        if not cliente['products']:
            print("   Sin productos registrados")
        else:
            for prod in cliente['products']:
                subtotal = prod['quantity'] * prod['price']
                print(f"   - {prod['productName']}: {prod['quantity']} x ${prod['price']:.2f} = ${subtotal:.2f}")
        
        total = servicio.obtener_total_cliente(id_cliente)
        print(f"\nTotal: ${total:.2f}")
        
    except ValueError:
        print("[ERROR] ID inválido.")

def ver_duplicados(servicio):
    """Muestra los duplicados encontrados"""
    duplicados = servicio.obtener_duplicados()
    
    print("\n" + "=" * 60)
    print("VERIFICACIÓN DE DUPLICADOS")
    print("=" * 60)
    
    if duplicados:
        print(f"Se encontraron {len(duplicados)} duplicado(s):\n")
        for dup in duplicados:
            print(f"[DUPLICADO] {dup}")
    else:
        print("[OK] No hay duplicados registrados.")

def cargar_datos_ejemplo(servicio):
    """Carga datos de ejemplo"""
    datos_ejemplo = [
        {
            'id': 1,
            'name': 'María',
            'email': 'maria@example.com',
            'products': [
                {'productName': 'Laptop', 'quantity': 1, 'price': 1200.00},
                {'productName': 'Smartphone', 'quantity': 2, 'price': 800.00},
            ]
        },
        {
            'id': 2,
            'name': 'Yorman',
            'email': 'yorman@example.com',
            'products': [
                {'productName': 'Smartphone', 'quantity': 2, 'price': 800.00},
                {'productName': 'Tablet', 'quantity': 5, 'price': 300.00}
            ]
        },
        {
            'id': 3,
            'name': 'Luis',
            'email': 'luis@example.com',
            'products': [
                {'productName': 'Printer', 'quantity': 1, 'price': 200.00},
            ]
        }
    ]
    
    print("\nCargando datos de ejemplo...")
    for datos in datos_ejemplo:
        cliente = servicio.agregar_cliente(
            datos['id'],
            datos['name'],
            datos['email'],
            datos['products']
        )
        if cliente:
            print(f"[OK] {cliente['name']} agregado")
    print("[OK] Datos de ejemplo cargados exitosamente.")

def main():
    """Función principal"""
    servicio = ClienteService()
    
    print("\n" + "=" * 60)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE CLIENTES")
    print("=" * 60)
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        if opcion == '1':
            agregar_cliente_interactivo(servicio)
        elif opcion == '2':
            listar_clientes_interactivo(servicio)
        elif opcion == '3':
            ver_detalles_cliente(servicio)
        elif opcion == '4':
            ver_duplicados(servicio)
        elif opcion == '5':
            cargar_datos_ejemplo(servicio)
        elif opcion == '6':
            print("\n[OK] ¡Hasta luego!")
            break
        else:
            print("[ERROR] Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()