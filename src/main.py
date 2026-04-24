"""Programa principal de demostración"""

import os
from service import ClientService


def main():
    # Ruta del archivo de datos
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')
    
    # Crear servicio
    service = ClientService(data_file)
    
    print("\n" + "="*60)
    print("🎯 SISTEMA DE GESTIÓN DE CLIENTES")
    print("="*60)
    
    # Agregar clientes
    print("\n📝 Agregando clientes...")
    service.add_client(1, "Juan Pérez", "juan@email.com", [
        {"nombre": "Laptop", "cantidad": 1, "precio": 1200.00},
        {"nombre": "Mouse", "cantidad": 2, "precio": 25.50}
    ])
    
    service.add_client(2, "María García", "maria@email.com", [
        {"nombre": "Monitor", "cantidad": 1, "precio": 350.00}
    ])
    
    service.add_client(3, "Carlos López", "carlos@email.com")
    
    # Intentar agregar duplicado (debe fallar)
    print("\n⚠️  Intentando agregar duplicado...")
    service.add_client(1, "Duplicado", "duplicado@email.com")  # Mismo ID
    service.add_client(4, "Otro", "juan@email.com")  # Mismo email
    
    # Agregar producto a cliente existente
    print("\n📦 Agregando producto a cliente...")
    service.add_product_to_client(3, "Teclado", 1, 75.00)
    service.add_product_to_client(3, "Pantalla", 2, 200.00)
    
    # Listar todos
    print("\n📊 Listando clientes...")
    service.list_clients()
    
    # Estadísticas
    stats = service.get_stats()
    print(f"\n📈 ESTADÍSTICAS")
    print(f"   Clientes: {stats['clientes']}")
    print(f"   Productos: {stats['productos']}")
    print(f"   Ingresos totales: ${stats['ingresos_totales']:.2f}")
    
    print("\n💾 Datos guardados automáticamente en: " + data_file)
    print("="*60 + "\n")


if __name__ == "__main__":
    main()