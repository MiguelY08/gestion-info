"""Servicio de gestión de clientes con persistencia"""

from validate import (
    validate_id, validate_name, validate_email,
    validate_product_name, validate_quantity, validate_price
)
from file import load_data, save_data


class ClientService:
    """Gestiona clientes y productos en memoria con persistencia JSON"""
    
    def __init__(self, filepath):
        """Inicializa el servicio con datos desde archivo"""
        self.filepath = filepath
        self.clients = load_data(filepath)
        self._init_sets()
    
    def _init_sets(self):
        """Inicializa sets de IDs y emails únicos"""
        self.client_ids = {c['id'] for c in self.clients}
        self.emails = {c['email'] for c in self.clients}
    
    def add_client(self, client_id, name, email, products=None):
        """
        Añade nuevo cliente con validaciones.
        Retorna True si es exitoso, False si hay error.
        """
        try:
            # Validar campos
            validate_id(client_id)
            validate_name(name)
            validate_email(email)
            
            # Verificar duplicados
            if client_id in self.client_ids:
                raise ValueError(f"ID {client_id} ya existe")
            if email in self.emails:
                raise ValueError(f"Email {email} ya está registrado")
            
            # Validar productos
            products = products or []
            for product in products:
                validate_product_name(product['nombre'])
                validate_quantity(product['cantidad'])
                validate_price(product['precio'])
            
            # Crear cliente
            client = {
                'id': client_id,
                'nombre': name,
                'email': email,
                'productos': products
            }
            
            # Añadir a memoria
            self.clients.append(client)
            self.client_ids.add(client_id)
            self.emails.add(email)
            
            # Guardar a archivo
            save_data(self.filepath, self.clients)
            print(f"✅ Cliente {name} añadido correctamente")
            return True
        
        except ValueError as e:
            print(f"❌ Error de validación: {e}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False
    
    def add_product_to_client(self, client_id, product_name, quantity, price):
        """Añade producto a cliente existente"""
        try:
            validate_product_name(product_name)
            validate_quantity(quantity)
            validate_price(price)
            
            client = self._find_client_by_id(client_id)
            if not client:
                raise ValueError(f"Cliente con ID {client_id} no existe")
            
            product = {
                'nombre': product_name,
                'cantidad': quantity,
                'precio': price
            }
            client['productos'].append(product)
            save_data(self.filepath, self.clients)
            print(f"✅ Producto '{product_name}' añadido a cliente {client_id}")
            return True
        
        except ValueError as e:
            print(f"❌ Error: {e}")
            return False
    
    def list_clients(self):
        """Lista todos los clientes"""
        if not self.clients:
            print("📭 No hay clientes registrados")
            return
        
        print(f"\n{'='*60}")
        print(f"📋 CLIENTES REGISTRADOS ({len(self.clients)})")
        print(f"{'='*60}")
        
        for client in self.clients:
            print(f"\n🧑 ID: {client['id']} | {client['nombre']}")
            print(f"   📧 Email: {client['email']}")
            
            if client['productos']:
                print(f"   📦 Productos ({len(client['productos'])})")
                for prod in client['productos']:
                    total = prod['cantidad'] * prod['precio']
                    print(f"      • {prod['nombre']}: {prod['cantidad']}x ${prod['precio']:.2f} (Total: ${total:.2f})")
            else:
                print(f"   📦 Sin productos")
    
    def get_client_by_email(self, email):
        """Obtiene cliente por email"""
        for client in self.clients:
            if client['email'] == email:
                return client
        return None
    
    def _find_client_by_id(self, client_id):
        """Encuentra cliente por ID"""
        for client in self.clients:
            if client['id'] == client_id:
                return client
        return None
    
    def get_stats(self):
        """Retorna estadísticas del sistema"""
        total_clients = len(self.clients)
        total_products = sum(len(c['productos']) for c in self.clients)
        total_revenue = sum(
            p['cantidad'] * p['precio']
            for c in self.clients
            for p in c['productos']
        )
        return {
            'clientes': total_clients,
            'productos': total_products,
            'ingresos_totales': total_revenue
        }
    
    def new_register(self, client_id, name, email):
        """
        Crea un nuevo registro de cliente.
        Retorna True si exitoso, False si error.
        """
        try:
            # Validar campos
            validate_id(client_id)
            validate_name(name)
            validate_email(email)
            
            # Verificar duplicados
            if client_id in self.client_ids:
                raise ValueError(f"ID {client_id} ya existe")
            if email in self.emails:
                raise ValueError(f"Email {email} ya está registrado")
            
            # Crear cliente
            client = {
                'id': client_id,
                'nombre': name,
                'email': email,
                'productos': []
            }
            
            # Añadir a memoria
            self.clients.append(client)
            self.client_ids.add(client_id)
            self.emails.add(email)
            
            # Guardar a archivo
            save_data(self.filepath, self.clients)
            print(f"✅ Registro creado: {name} (ID: {client_id})")
            return True
        
        except ValueError as e:
            print(f"❌ Error de validación: {e}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False
    
    def list_records(self):
        """Lista todos los registros ordenados por nombre usando lambda"""
        if not self.clients:
            print("📭 No hay registros")
            return
        
        # Ordenar por nombre usando lambda
        sorted_clients = sorted(self.clients, key=lambda c: c['nombre'])
        
        print(f"\n{'='*60}")
        print(f"📋 REGISTROS ({len(sorted_clients)})")
        print(f"{'='*60}")
        
        for client in sorted_clients:
            print(f"\n🧑 ID: {client['id']} | {client['nombre']}")
            print(f"   📧 Email: {client['email']}")
            if client['productos']:
                print(f"   📦 Productos: {len(client['productos'])}")
            else:
                print("   📦 Sin productos")
    
    def search_record(self, client_id):
        """Busca registro por ID usando list comprehension"""
        try:
            validate_id(client_id)
            
            # Usar list comprehension para encontrar el cliente
            found_clients = [c for c in self.clients if c['id'] == client_id]
            
            if not found_clients:
                print(f"❌ Registro con ID {client_id} no encontrado")
                return None
            
            client = found_clients[0]
            print(f"✅ Registro encontrado:")
            print(f"   🧑 ID: {client['id']} | {client['nombre']}")
            print(f"   📧 Email: {client['email']}")
            if client['productos']:
                print(f"   📦 Productos ({len(client['productos'])})")
                for prod in client['productos']:
                    total = prod['cantidad'] * prod['precio']
                    print(f"      • {prod['nombre']}: {prod['cantidad']}x ${prod['precio']:.2f} (Total: ${total:.2f})")
            else:
                print("   📦 Sin productos")
            return client
        
        except ValueError as e:
            print(f"❌ Error: {e}")
            return None
    
    def update_record(self, client_id, name=None, email=None):
        """
        Actualiza registro por ID.
        Solo actualiza campos proporcionados.
        """
        try:
            validate_id(client_id)
            
            client = self._find_client_by_id(client_id)
            if not client:
                raise ValueError(f"Registro con ID {client_id} no existe")
            
            updated = False
            
            if name is not None:
                validate_name(name)
                client['nombre'] = name
                updated = True
            
            if email is not None:
                validate_email(email)
                # Verificar si email ya existe en otro cliente
                if email != client['email'] and email in self.emails:
                    raise ValueError(f"Email {email} ya está registrado")
                if email != client['email']:
                    self.emails.remove(client['email'])
                    self.emails.add(email)
                    client['email'] = email
                    updated = True
            
            if updated:
                save_data(self.filepath, self.clients)
                print(f"✅ Registro {client_id} actualizado")
                return True
            else:
                print(f"ℹ️  No se realizaron cambios en registro {client_id}")
                return True
        
        except ValueError as e:
            print(f"❌ Error: {e}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False
    
    def delete_record(self, client_id):
        """Elimina registro por ID"""
        try:
            validate_id(client_id)
            
            client = self._find_client_by_id(client_id)
            if not client:
                raise ValueError(f"Registro con ID {client_id} no existe")
            
            # Remover de memoria
            self.clients.remove(client)
            self.client_ids.remove(client_id)
            self.emails.remove(client['email'])
            
            # Guardar cambios
            save_data(self.filepath, self.clients)
            print(f"✅ Registro {client_id} ({client['nombre']}) eliminado")
            return True
        
        except ValueError as e:
            print(f"❌ Error: {e}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False