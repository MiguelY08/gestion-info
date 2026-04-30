"""Programa principal con menú interactivo"""

import os
from service import ClientService
from menu import MenuInteractivo


def main():
    # Ruta del archivo de datos
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')
    
    # Crear servicio
    service = ClientService(data_file)
    
    # Crear y ejecutar menú
    menu = MenuInteractivo(service)
    menu.ejecutar()
    
    print("\n Datos guardados automáticamente en: " + data_file)
    print("="*60 + "\n")


if __name__ == "__main__":
    main()