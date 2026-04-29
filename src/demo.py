"""
Demostración del sistema de gestión con menú interactivo.
Este script muestra todas las funcionalidades.
"""

import os
from service import ClientService
from menu import MenuInteractivo


def demo():
    """Ejecuta una demostración de prueba"""
    
    # Ruta del archivo de datos
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')
    
    # Crear servicio
    service = ClientService(data_file)
    
    # Crear algunos registros de prueba si la base está vacía
    if len(service.clients) == 0:
        print("\n📝 Creando registros de prueba...\n")
        service.new_register(1, "Juan Pérez", "juan@email.com")
        service.new_register(2, "María García", "maria@email.com")
        service.new_register(3, "Carlos López", "carlos@email.com")
    
    # Mostrar estadísticas iniciales
    stats = service.get_stats()
    print(f"\n📊 Estado actual: {stats['clientes']} cliente(s)\n")
    
    # Crear y ejecutar menú
    menu = MenuInteractivo(service)
    menu.ejecutar()


if __name__ == "__main__":
    demo()
