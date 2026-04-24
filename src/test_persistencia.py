"""Prueba 1: Carga de datos persistentes"""

import os
from service import ClientService


def main():
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')
    
    print("\n" + "="*60)
    print("🔄 PRUEBA 1: CARGA DE DATOS PERSISTENTES")
    print("="*60)
    
    # Crear servicio (cargará datos existentes)
    service = ClientService(data_file)
    
    # Listar datos cargados
    print("\n📊 Datos cargados del archivo:")
    service.list_clients()
    
    # Estadísticas
    stats = service.get_stats()
    print(f"\n📈 ESTADÍSTICAS")
    print(f"   Clientes: {stats['clientes']}")
    print(f"   Productos: {stats['productos']}")
    print(f"   Ingresos totales: ${stats['ingresos_totales']:.2f}")
    
    print("\n✅ Los datos persisten correctamente entre ejecuciones")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
