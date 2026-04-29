"""Menú interactivo en consola con colorama"""

from colorama import Fore, Back, Style, init
from service import ClientService
import os

# Inicializar colorama
init(autoreset=True)


class MenuInteractivo:
    """Gestiona el menú interactivo del sistema"""
    
    def __init__(self, service):
        """Inicializa el menú con el servicio"""
        self.service = service
        self.ejecutando = True
    
    def mostrar_titulo(self):
        """Muestra el título principal con colores"""
        print("\n" + Fore.CYAN + "="*60)
        print(Fore.CYAN + " SISTEMA DE GESTIÓN DE CLIENTES")
        print(Fore.CYAN + "="*60 + Style.RESET_ALL)
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal con opciones"""
        print("\n" + Fore.YELLOW + " MENÚ PRINCIPAL" + Style.RESET_ALL)
        print(Fore.GREEN + "1" + Style.RESET_ALL + ".  Crear nuevo registro")
        print(Fore.GREEN + "2" + Style.RESET_ALL + ".  Listar todos los registros")
        print(Fore.GREEN + "3" + Style.RESET_ALL + ".  Buscar registro por ID")
        print(Fore.GREEN + "4" + Style.RESET_ALL + ".   Editar registro")
        print(Fore.GREEN + "5" + Style.RESET_ALL + ".   Eliminar registro")
        print(Fore.GREEN + "6" + Style.RESET_ALL + ".  Ver estadísticas")
        print(Fore.RED + "0" + Style.RESET_ALL + ".  Salir")
        print(Fore.CYAN + "-"*60 + Style.RESET_ALL)
    
    def obtener_opcion(self):
        """Obtiene la opción del usuario con manejo de errores"""
        while True:
            try:
                opcion = input(Fore.MAGENTA + "Ingrese su opción: " + Style.RESET_ALL).strip()
                return int(opcion)
            except ValueError:
                print(Fore.RED + "❌ Error: Ingrese un número válido" + Style.RESET_ALL)
            except KeyboardInterrupt:
                print(Fore.YELLOW + "\n⚠️  Operación cancelada por el usuario" + Style.RESET_ALL)
                return 0  # Salir del programa    
    def crear_registro(self):
        """Opción: Crear nuevo registro"""
        print("\n" + Fore.YELLOW + "CREAR NUEVO REGISTRO" + Style.RESET_ALL)
        
        try:
            # Obtener ID
            while True:
                try:
                    client_id = int(input(Fore.MAGENTA + "ID del cliente: " + Style.RESET_ALL))
                    break
                except ValueError:
                    print(Fore.RED + " El ID debe ser un número" + Style.RESET_ALL)
            
            # Obtener nombre
            nombre = input(Fore.MAGENTA + "Nombre del cliente: " + Style.RESET_ALL).strip()
            
            # Obtener email
            email = input(Fore.MAGENTA + "Email del cliente: " + Style.RESET_ALL).strip()
            
            # Crear registro
            if self.service.new_register(client_id, nombre, email):
                print(Fore.GREEN + "Registro creado exitosamente" + Style.RESET_ALL)
                return True
            return False
        
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n Operación cancelada" + Style.RESET_ALL)
            return False
        except Exception as e:
            print(Fore.RED + f" Error inesperado: {e}" + Style.RESET_ALL)
            return False
    
    def listar_registros(self):
        """Opción: Listar todos los registros"""
        print("\n" + Fore.YELLOW + " LISTADO DE REGISTROS" + Style.RESET_ALL)
        self.service.list_records()
    
    def buscar_registro(self):
        """Opción: Buscar registro por ID"""
        print("\n" + Fore.YELLOW + "BUSCAR REGISTRO" + Style.RESET_ALL)
        
        try:
            while True:
                try:
                    client_id = int(input(Fore.MAGENTA + "ID del cliente a buscar: " + Style.RESET_ALL))
                    break
                except ValueError:
                    print(Fore.RED + " El ID debe ser un número" + Style.RESET_ALL)
            
            self.service.search_record(client_id)
        
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n Búsqueda cancelada" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f" Error: {e}" + Style.RESET_ALL)

    def editar_registro(self):
        """Opción: Editar registro existente"""
        print("\n" + Fore.YELLOW + "  EDITAR REGISTRO" + Style.RESET_ALL)
        
        try:
            # Obtener ID
            while True:
                try:
                    client_id = int(input(Fore.MAGENTA + "ID del cliente a editar: " + Style.RESET_ALL))
                    break
                except ValueError:
                    print(Fore.RED + " El ID debe ser un número" + Style.RESET_ALL)
            
            # Verificar que exista
            if not self.service._find_client_by_id(client_id):
                print(Fore.RED + f" Cliente con ID {client_id} no existe" + Style.RESET_ALL)
                return False
            
            # Mostrar opciones de edición
            print(Fore.CYAN + "\n¿Qué desea editar?" + Style.RESET_ALL)
            print("1. Nombre")
            print("2. Email")
            print("3. Ambos")
            
            while True:
                try:
                    opcion = int(input(Fore.MAGENTA + "Opción: " + Style.RESET_ALL))
                    if opcion in [1, 2, 3]:
                        break
                    print(Fore.RED + "❌ Opción no válida (1-3)" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "❌ Ingrese un número válido" + Style.RESET_ALL)
            
            nombre = None
            email = None
            
            if opcion in [1, 3]:
                nombre = input(Fore.MAGENTA + "Nuevo nombre: " + Style.RESET_ALL).strip()
            
            if opcion in [2, 3]:
                email = input(Fore.MAGENTA + "Nuevo email: " + Style.RESET_ALL).strip()
            
            # Actualizar registro
            if self.service.update_record(client_id, nombre, email):
                print(Fore.GREEN + " Registro actualizado exitosamente" + Style.RESET_ALL)
                return True
            return False
        
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n Edición cancelada" + Style.RESET_ALL)
            return False
        except Exception as e:
            print(Fore.RED + f" Error: {e}" + Style.RESET_ALL)
            return False
    
    def eliminar_registro(self):
        """Opción: Eliminar registro"""
        print("\n" + Fore.YELLOW + "  ELIMINAR REGISTRO" + Style.RESET_ALL)
    
        try:
            # Obtener ID
            while True:
                try:
                    client_id = int(input(Fore.MAGENTA + "ID del cliente a eliminar: " + Style.RESET_ALL))
                    break
                except ValueError:
                    print(Fore.RED + "El ID debe ser un número" + Style.RESET_ALL)
            
            # Confirmación
            confirmacion = input(
                Fore.YELLOW + f"  ¿Confirma eliminar el cliente {client_id}? (s/n): " + Style.RESET_ALL
            ).strip().lower()
            
            if confirmacion == 's':
                if self.service.delete_record(client_id):
                    print(Fore.GREEN + " Registro eliminado exitosamente" + Style.RESET_ALL)
                    return True
                return False
            else:
                print(Fore.YELLOW + "Operación cancelada" + Style.RESET_ALL)
                return False
        
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n Eliminación cancelada" + Style.RESET_ALL)
            return False
        except Exception as e:
            print(Fore.RED + f" Error: {e}" + Style.RESET_ALL)
            return False
    
    def mostrar_estadisticas(self):
        """Opción: Mostrar estadísticas"""
        print("\n" + Fore.YELLOW + " ESTADÍSTICAS DEL SISTEMA" + Style.RESET_ALL)
        
        stats = self.service.get_stats()
        print(Fore.CYAN + "="*60)
        print(f"   👥 Clientes registrados: {Fore.GREEN}{stats['clientes']}")
        print(f"   {Fore.CYAN} Productos totales: {Fore.GREEN}{stats['productos']}")
        print(f"   {Fore.CYAN} Ingresos totales: {Fore.GREEN}${stats['ingresos_totales']:.2f}")
        print(Fore.CYAN + "="*60 + Style.RESET_ALL)
    
    def ejecutar(self):
        """Bucle principal del menú"""
        self.mostrar_titulo()
        
        try:
            while self.ejecutando:
                self.mostrar_menu_principal()
                opcion = self.obtener_opcion()
                
                if opcion == 1:
                    self.crear_registro()
                elif opcion == 2:
                    self.listar_registros()
                elif opcion == 3:
                    self.buscar_registro()
                elif opcion == 4:
                    self.editar_registro()
                elif opcion == 5:
                    self.eliminar_registro()
                elif opcion == 6:
                    self.mostrar_estadisticas()
                elif opcion == 0:
                    self.salir()
                else:
                    print(Fore.RED + "❌ Opción no válida. Ingrese 0-6" + Style.RESET_ALL)
                
                # Pausa para lectura
                if self.ejecutando:  # Solo mostrar si no estamos saliendo
                    input(Fore.CYAN + "\nPresione Enter para continuar..." + Style.RESET_ALL)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n⚠️  Programa interrumpido por el usuario" + Style.RESET_ALL)
            self.salir()
    
    def salir(self):
        """Opción: Salir del programa"""
        print("\n" + Fore.CYAN + "="*60)
        print(Fore.YELLOW + " ¡Gracias por usar el sistema de gestión!")
        print(Fore.CYAN + "="*60 + Style.RESET_ALL)
        self.ejecutando = False


if __name__ == "__main__":
    """Punto de entrada para ejecutar el menú directamente"""
    # Ruta del archivo de datos
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')
    
    # Crear servicio
    service = ClientService(data_file)
    
    # Crear y ejecutar menú
    menu = MenuInteractivo(service)
    menu.ejecutar()
    
    print("\n Datos guardados automáticamente en: " + data_file)
    print("="*60 + "\n")
